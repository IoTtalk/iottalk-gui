import json

from django.db.transaction import atomic
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin

from braces.views import CsrfExemptMixin, JSONResponseMixin, JSONRequestResponseMixin

from dev_model.models import Dev, DevModel, Feature
from proj.models import Graph


class DevModelListView(JSONResponseMixin, ListView):
    model = DevModel

    def get(self, request):
        context = self.get_context_data()
        return self.render_json_response(context)

    def get_context_data(self):
        return tuple(obj.json for obj in self.get_queryset())


class DevSingleView(CsrfExemptMixin, JSONRequestResponseMixin,
                    SingleObjectMixin, View):
    model = Dev
    require_json = True
    error_response_dict = {'state': 'error', 'reason': 'invalid json'}

    def put(self, request, pk=None):
        '''
        Create the model instance (``dev_model.models.Dev``)

        Expect request schema::

            {
                'model': 'pk of model',
                'idf': [list of enabled idf pk],
                'odf': [list of enabled odf pk],
                'graph': 'pk of graph',
            }
        '''
        if pk is not None:
            return self.render_bad_request_response('invalid url')

        try:
            self.validate_put_schema(self.request_json)
        except ValueError as err:
            return self.render_bad_request_response(str(err))

        try:
            model = self.get_or_404(DevModel, pk=self.request_json['model'])
            graph = self.get_or_404(Graph, pk=self.request_json['graph'])
            idf = [self.get_or_404(Feature, pk=pk, type='i', mod=model)
                for pk in self.request_json['idf']]
            odf = [self.get_or_404(Feature, pk=pk, type='o', mod=model)
                for pk in self.request_json['odf']]
        except Http404 as err:
            return self.render_404(str(err))

        if not idf and not odf:
            return self.render_404('Require at least one of idf or odf')

        device_i, device_o = None, None
        with atomic():
            if idf:
                device_i = Dev.objects.create(mod=model, graph=graph, type='i')
                for feature in idf:
                    device_i.feature_set.add(feature)
            if odf:
                device_o = Dev.objects.create(mod=model, graph=graph, type='o')
                for feature in odf:
                    device_o.feature_set.add(feature)

            # link them via ``pair``
            if idf and odf:
                device_i.pair = device_o
                device_o.pair = device_i

                device_i.save()
                device_o.save()

        return self.render_json_response({
            'state': 'ok',
            'input':  device_i.json if device_i else None,
            'output': device_o.json if device_o else None,
        })

    @staticmethod
    def validate_put_schema(payload):
        if set(payload.keys()) != set(('model', 'idf', 'odf', 'graph')):
            raise ValueError('invalid json')

    def render_bad_request_response(self, reason=None):
        return super(type(self), self).render_json_response(
            self.error_dict(reason) if reason else None)

    def render_404(self, reason='Not Found'):
        payload = json.dumps(self.error_dict(reason=reason)).encode('utf-8')
        return HttpResponseNotFound(
            payload, content_type=self.get_content_type())

    @staticmethod
    def error_dict(reason):
        '''
        Get the consistant error json response
        '''
        return {
            'state': 'error',
            'reason': reason,
        }

    @staticmethod
    def get_or_404(model, **query):
        '''
        :return: the object or HttpResponseNotFound
        '''
        try:
            return model.objects.get(**query)
        except model.DoesNotExist as err:
            raise Http404(str(err))
