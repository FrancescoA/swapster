from django.conf.urls import patterns, url

from objects.views import ObjectDetailView

urlpatterns = patterns('',
    url(r'^detail/$', ObjectDetailView.as_view(), name='object-detail'),
)