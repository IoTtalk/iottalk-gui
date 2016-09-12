from django.shortcuts import render
from django.views.generic import DetailView

from braces.views import JSONResponseMixin

from dev_model.models import Dev


class ProjDetailView(JSONResponseMixin, DetailView):
    # TBD:
    # model = Project

    def get(self, request, pid):
        '''
        :param pid: project id
        '''
        # TBD: remove mock data

        alpha_cat_i = Dev.objects.get(pk=1)
        alpha_cat_o = Dev.objects.get(pk=10)
        beta_cat = Dev.objects.get(pk=8)
        mor_sensor = Dev.objects.get(pk=9)

        context = {
            'graphs': [1, 2],
            'pid': pid,
            'ref' :{
                'models': {  # actually it's decive models instance
                    dev.pk: dev.json
                    for dev in (alpha_cat_i, alpha_cat_o, beta_cat, mor_sensor)
                },
                'graphs': {
                    1: {
                        'pk': 1,
                        'input': [1],
                        'output': [8],
                    },
                    2: {
                        'pk': 2,
                        'input': [9],
                        'output': [10],
                    }
                },
            }
        }
        return self.render_json_response(context)
