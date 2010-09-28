from django.shortcuts import render_to_response
from models import Person
from django.template import RequestContext
from bio.context_processor import get_settings

def index(request):
    person = Person.objects.all()[0]  #first person in DB       
    #get list (verbose_name,value) for object
    person_data = []
    for field in person._meta.fields:
        key = field.verbose_name
        value = person.__getattribute__(field.name)
        if key == 'ID':
            continue
        person_data.append((key, value))
                         
    return render_to_response('bio/index.html', 
                        {'person': person_data}, 
                        context_instance = RequestContext(request))

def settings(request):
    context = RequestContext(request, {}, [get_settings])
    return render_to_response('settings.html', context_instance = context)