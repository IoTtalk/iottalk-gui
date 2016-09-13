from django.conf.urls import url

from proj.views import ProjDetailView


urlpatterns = (
    url(r'^(?P<pk>[\d]+)/', ProjDetailView.as_view(), name='detail'),
)
