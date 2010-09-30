from django.conf.urls.defaults import *
from bio.views import index, settings, edit_person

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
    (r'^settings/$', settings),
    (r'^edit/$', edit_person),
)
