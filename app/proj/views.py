from itertools import chain

from django.shortcuts import render
from django.views.generic import DetailView

from braces.views import JSONResponseMixin

from dev_model.models import Dev
from proj.models import Project


class ProjDetailView(JSONResponseMixin, DetailView):
    model = Project

    def get(self, request, pk):
        '''
        :param pid: project id
        '''
        proj = self.get_object()
        graph_set = proj.graph_set.all()
        dev_set = chain(*(graph.dev_set.all() for graph in graph_set))

        context = {
            'graphs': tuple(g.pk for g in graph_set),
            'proj': proj.json,
            'ref' :{
                'models': {  # actually it's decive models instance
                    dev.pk: dev.json for dev in dev_set
                },
                'graphs': {
                    graph.pk: graph.json for graph in graph_set
                },
            }
        }
        return self.render_json_response(context)
