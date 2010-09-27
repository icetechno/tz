from django.forms import ModelForm
from models import Person
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Textarea

# Create the form class.
class PersonForm(ModelForm):   
    birthdate = forms.DateField(widget=SelectDateWidget())
    
    class Meta:
        model = Person
        widgets = {
            'contacts': Textarea(attrs={'cols': 40, 'rows': 2}),
        }

# Create the form class.
class PersonDetail(ModelForm):           
    class Meta:
        model = Person
        widgets = {
            'contacts': Textarea(attrs={'cols': 40, 'rows': 2}),
        }