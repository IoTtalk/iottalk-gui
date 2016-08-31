from tornado.web import  HTTPError, RequestHandler
from tornado.escape import json_decode, json_encode


class JSONHandler(RequestHandler):

    def prepare(self):
        if self.request.method in ('GET', 'OPTIONS', 'HEAD', 'DELETE'):
            return

        content_type = self.request.headers.get('Content-Type', '')

        if not content_type.startswith('application/json'):
            self.send_error(
                400, msg='content type not supported: {!r}'.format(
                          content_type))

        try:
            self.json = json_decode(self.request.body)
        except ValueError:
            self.send_error(400, msg='json decode error')

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def write(self, obj):
        '''
        Write a dictionary as json to response
        '''
        if not isinstance(obj, dict):
            raise TypeError('Object {!r} is not a dict'.format(obj))

        super(JSONHandler, self).write(json_encode(obj))
        self.finish()

    def write_error(self, status_code, msg=None, **kwargs):
        self.write({
            'state': 'error',
            'reason': msg or 'unkown',
        })


class MainHandler(RequestHandler):
    def get(self):
        self.render('base.html')


class ProjectHandler(JSONHandler):

    def initialize(self, db):
        self.db = db

    def get(self, pid=None):
        '''
        :param pid: the project id
        '''
        if not pid:
            self.send_error(404, msg='unkown project id')

        alpha_cat = {'odf': ['meow']}
        beta_cat = {'idf': ['meow']}
        mor_sensor = {'idf': ['acce', 'temp']}

        self.write({
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
        })

    def put(self, pid=None):
        '''
        create a new project

        :response: {
            'pid': 'the project id',
        }
        '''
        self.write({
            'pid': 1,
        })
