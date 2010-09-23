from django.contrib import admin
from tz_42cc.bio.models import Person, HttpRequestData

admin.site.register(Person)
admin.site.register(HttpRequestData)