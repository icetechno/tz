from django.shortcuts import render_to_response
from tz_42cc.bio.models import Person
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from tz_42cc.bio.context_processor import get_settings
from tz_42cc.bio.model_form import PersonForm


def start_page(request):
    return render_to_response('links.html', {})

def index(request):
    persons_data = Person.objects.all()
    return render_to_response('bio/index.html', {'persons_data': persons_data})

@login_required
def edit_person(request):
    first_person = Person.objects.all()[0]  #first person in DB       
    form = PersonForm(instance = first_person) 
    if request.method == 'POST':  #recived post data to save  
        form = PersonForm(request.POST, instance = first_person) #load post data into object
        if form.is_valid(): #if form data are valid
            form.save()     #save data from object to DB
        else: # form data not valid
            return render_to_response('bio/edit_error.html')
    
    return render_to_response('bio/edit.html', 
                              {'form': form}, 
                              context_instance = RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/bio')

def settings(request):
    context = RequestContext(request, {}, [get_settings])
    return render_to_response('settings.html', context_instance = context)

def test_tag(request):
    return render_to_response('test_tag.html', {'request': request}, context_instance = RequestContext(request))