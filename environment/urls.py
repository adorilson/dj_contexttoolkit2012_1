from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

from environment.models import Estatistica


class EstatisticaResource(ModelResource):
    model = Estatistica


urlpatterns = patterns('',
    url(r'^rest/environment/$', ListOrCreateModelView.as_view(resource=EstatisticaResource)),
    url(r'^rest/environment/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=EstatisticaResource)),
)

