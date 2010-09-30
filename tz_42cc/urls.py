from django.conf.urls.defaults import *
from bio.views import index

from django.contrib import admin
admin.autodiscover()

from bio.views import settings

urlpatterns = patterns('',
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
    (r'^settings/$', settings),
)
