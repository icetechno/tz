from django.forms import ModelForm
from tz_42cc.bio.models import Person
from django import forms
from django.forms.extras.widgets import SelectDateWidget

# Create the form class.
class PersonForm(ModelForm):   
    birthdate = forms.DateField(widget=SelectDateWidget())
    def __init__(self, *args, **kw): 
        super(ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse() 
    
    class Meta:
        model = Person