from django.forms import ModelForm
from models import Person
from django import forms
from widgets import CalendarWidget


# Create the form class.
class PersonForm(ModelForm):
    birthdate = forms.DateField(widget=CalendarWidget())

    class Meta:
        model = Person
