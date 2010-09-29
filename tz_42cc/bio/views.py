from django.shortcuts import render_to_response
from models import Person, HttpRequestData
from django.contrib.auth.decorators import login_required
from model_form import PersonForm
from django.template import RequestContext
from context_processor import get_settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

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
                        {'person': person_data, 'request': request}, 
                        context_instance = RequestContext(request))

def settings(request):
    context = RequestContext(request, {}, [get_settings])
    return render_to_response('settings.html', context_instance = context)

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
    return HttpResponseRedirect('/')

def settings(request):
    context = RequestContext(request, {}, [get_settings])
    return render_to_response('settings.html', context_instance = context)

def test_tag(request):
    return render_to_response('test_tag.html', {'request': request}, context_instance = RequestContext(request))

def loglist(request):
    log_list = HttpRequestData.objects.all()[:10]
    return render_to_response('log_list.html', {'log_list' : log_list})
