from django.shortcuts import render_to_response
from models import Person
from model_form import PersonDetail
from django.template import RequestContext

def index(request):
    first_person = Person.objects.all()[0]  #first person in DB       
    form = PersonDetail(instance = first_person)     
    return render_to_response('bio/index.html', 
                        {'form': form}, 
                        context_instance = RequestContext(request))

def start_page(request):
    return render_to_response('links.html',
                        {},
                        context_instance = RequestContext(request))
