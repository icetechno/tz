from django.forms import ModelForm, Textarea
from models import Person
from django import forms
from widgets import CalendarWidget
from django.core.validators import BaseValidator


# Create the form class.
class PersonForm(ModelForm):
    birthdate = forms.DateField(widget=CalendarWidget())

    def __init__(self, *args, **kw):
        super(ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()

    class Meta:
        model = Person
