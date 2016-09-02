from django.shortcuts import render
from django.views.generic import DetailView

from braces.views import JSONResponseMixin


class ProjDetailView(JSONResponseMixin, DetailView):
    # TBD:
    # model = Project

    def get(self, request, pid):
        '''
        :param pid: project id
        '''
        # TBD: remove mock data
        alpha_cat = {
            'name': 'AlphaCat',
            'odf': [
                {
                    'name': 'meow',
                    'enable': True,
                    'func': None
                },
            ],
        }
        beta_cat = {
            'name': 'BetaCat',
            'idf': [
                {
                    'name': 'meow',
                    'enable': True,
                    'func': None
                },
            ],
        }
        mor_sensor = {
            'name': 'MorSensor',
            'idf': [
                {
                    'name': 'acce',
                    'enable': True,
                    'func': None
                },
                {
                    'name': 'temp',
                    'enable': True,
                    'func': None
                },
                {
                    'name': 'color',
                    'enable': False,
                    'func': None
                },
            ],
        }

        context = {
            'graphs': [
                {
                    'idf': [
                        {'name': 'BetaCat', 'features': ['meow']}
                    ],
                    'odf': [
                        {'name': 'AlphaCat', 'features': ['meow']}
                    ],
                },
                {
                    'idf': [
                        {'name': 'MorSensor', 'features': ['acce', 'temp']}
                    ],
                    'odf': [
                        {'name': 'AlphaCat', 'features': ['meow']}
                    ],
                },
            ],
            'pid': pid,
            'models': {
                'AlphaCat': alpha_cat,
                'BetaCat': beta_cat,
                'MorSensor': mor_sensor,
            }
        }
        return self.render_json_response(context)

