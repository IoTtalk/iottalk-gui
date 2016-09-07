from django.conf.urls import url

from dev_model.views import DevModelListView

urlpatterns = (
    url(r'^$', DevModelListView.as_view(), name='list'),
)
