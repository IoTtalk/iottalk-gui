from django.shortcuts import render
from django.views.generic import ListView

from braces.views import JSONResponseMixin

from dev_model.models import DevModel


class DevModelListView(JSONResponseMixin, ListView):
    model = DevModel

    def get(self, request):
        context = self.get_context_data()
        print(context[0])
        return self.render_json_response(context)

    def get_context_data(self):
        return tuple(obj.json for obj in self.get_queryset())
