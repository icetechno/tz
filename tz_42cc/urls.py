from django.conf import settings as django_settings
from django.conf.urls.defaults import *
from django.contrib import admin

from bio.views import index, settings, edit_person, logout_user, loglist

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index),
    (r'^edit/$', edit_person),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_user),
    (r'^settings/$', settings),
    (r'^loglist/$', loglist),
    (r'^site_media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': django_settings.MEDIA_ROOT}),
    (r'^edit/$', edit_person),
    (r'^site_media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': django_settings.MEDIA_ROOT}),
)
