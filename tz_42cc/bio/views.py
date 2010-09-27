from django.shortcuts import render_to_response
from models import Person
from model_form import PersonDetail
from django.template import RequestContext
from bio.context_processor import get_settings

def index(request):
    first_person = Person.objects.all()[0]  #first person in DB       
    form = PersonDetail(instance = first_person)     
    return render_to_response('bio/index.html', 
                        {'form': form}, 
                        context_instance = RequestContext(request))

def settings(request):
    context = RequestContext(request, {}, [get_settings])
    return render_to_response('settings.html', context_instance = context)

def start_page(request):
    return render_to_response('links.html',
                        {},
                        context_instance = RequestContext(request))