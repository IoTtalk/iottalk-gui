import socket

from django.shortcuts import render
from django.views import View

from braces.views import JSONResponseMixin


def index(request):
    return render(request, 'base.html')


class MQTTConfView(JSONResponseMixin, View):

    def get(self, request):
        '''
        .. TODO::
            - configurable
        '''
        return self.render_json_response({
            'scheme': 'ws',
            'host': self.local_ip,
            'port': 9000,
        })

    @property
    def local_ip(self):
        return [
            (s.connect(('8.8.8.8', 53)),
             s.getsockname()[0],
             s.close())
            for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
