from django.shortcuts import render_to_response
from tz_42cc.bio.models import Person

def index(request):
    persons_data = Person.objects.all()
    return render_to_response('bio/index.html', {'persons_data': persons_data})

def start_page(request):
    return render_to_response('links.html', {})
