from django.conf.urls.defaults import *
from bio.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
)
