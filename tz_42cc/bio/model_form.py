# -*- coding: utf-8 -*-
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
    
    def ajax_response(self):
        return u'<table>%s</table>\
        <input type="submit" value="Редактировать">' % self.as_table()
    
    class Meta:
        model = Person
