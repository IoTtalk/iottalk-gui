from django.conf.urls import url

from dev_model.views import DevModelListView, DevSingleView

urlpatterns = (
    url(r'^$', DevModelListView.as_view(), name='list'),
    url(r'^obj/(?:(?P<pk>[\d]+)/)?$', DevSingleView.as_view(), name='obj')
)
