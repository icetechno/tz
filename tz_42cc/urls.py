from django.conf.urls.defaults import *
from bio.views import index, settings, edit_person, logout_user
from django.conf import settings as django_settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_user),
    (r'^settings/$', settings),
    (r'^edit/$', edit_person),
    (r'^site_media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': django_settings.MEDIA_ROOT}),
)
