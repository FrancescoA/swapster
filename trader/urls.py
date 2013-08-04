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
    url(r'^profile/','trader.views.profile'),
    url(r'^edit/', UpdateTraderView.as_view())
)
