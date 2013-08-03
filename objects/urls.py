from django.conf.urls import patterns, url

from objects.views import ObjectDetailView, ObjectCreateView


urlpatterns = patterns('',
    url(r'^detail/$', ObjectDetailView.as_view(), name='object-detail'),
    url(r'^add/$', ObjectCreateView.as_view(), name='object-create')
)