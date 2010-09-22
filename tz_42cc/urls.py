from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tz_42cc.bio.views import start_page, logout_user, settings, test_tag

urlpatterns = patterns('',
    # Example:
    # (r'^tz_42cc/', include('tz_42cc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', start_page),
    (r'^bio/', include('tz_42cc.bio.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_user),
    (r'^settings/$', settings),
    (r'^test_tag/$', test_tag),
)
