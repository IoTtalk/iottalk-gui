from django.conf.urls import url

from iottalk.views import MQTTConfView

urlpatterns = (
    url(r'^mqtt/', MQTTConfView.as_view(), name='mqtt'),
)
