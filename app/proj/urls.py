from django.conf.urls import url

from proj.views import ProjDetailView


urlpatterns = (
    url(r'^(?P<pid>[\d]+)/', ProjDetailView.as_view(), name='detail'),
)
