from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swapster.views.home', name='home'),
    # url(r'^swapster/', include('swapster.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'swapster.views.index',),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^traders/', include('trader.urls')),
    url(r'^objects/', include('objects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
