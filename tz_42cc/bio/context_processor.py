from django.conf import settings

def get_settings(request):
    #extract values
    django_settings = {}
    for setting in dir(settings):
        if setting.isupper():
            django_settings[setting] = getattr(settings, setting)
            
    return {'settings' : django_settings}