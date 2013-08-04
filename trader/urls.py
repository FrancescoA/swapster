from django.conf.urls import patterns, include, url
from trader.views import UpdateTraderView

# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swapster.views.home', name='home'),
    # url(r'^swapster/', include('swapster.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/', 'trader.views.login',),
    url(r'^profile/', UpdateTraderView.as_view(), name='user_profile'),
    url(r'^(?P<username>\w+)/$', 'trader.views.profile', name='generic_profile'),
    url(r'^(?P<username>\w+)/trade/$', 'trader.views.tradeview', name='trade'),
    url(r'^(?P<username>\w+)/trade/makeoffer/$'), 'trader.views.offer', name='makeoffer'),
)