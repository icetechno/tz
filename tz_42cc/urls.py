from django.conf.urls.defaults import *
from bio.views import start_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from bio.views import settings

urlpatterns = patterns('',
    (r'^$', start_page),                       
    # Example:
    # (r'^tz_42cc/', include('tz_42cc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^bio/', include('tz_42cc.bio.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^settings/$', settings),
)
