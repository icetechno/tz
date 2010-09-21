from django.shortcuts import render_to_response
from tz_42cc.bio.models import Person
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def index(request):
    persons_data = Person.objects.all()
    return render_to_response('bio/index.html', {'persons_data': persons_data})

@login_required
def edit_person(request):
    persons_data = Person.objects.all()
    return render_to_response('bio/index.html', 
                              {'persons_data': persons_data},
                              context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/bio')