from django.forms import ModelForm
from tz_42cc.bio.models import Person
from django import forms
from django.forms.extras.widgets import SelectDateWidget

# Create the form class.
class PersonForm(ModelForm):   
    birthdate = forms.DateField(widget=SelectDateWidget())
    
    class Meta:
        model = Person
    
