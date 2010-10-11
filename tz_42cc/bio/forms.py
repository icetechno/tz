# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import BaseValidator
from django.forms import ModelForm, Textarea

from models import Person
from widgets import CalendarWidget


# Create the form class.
class PersonForm(ModelForm):
    birthdate = forms.DateField(widget=CalendarWidget())

    def __init__(self, *args, **kw):
        super(ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()

    def ajax_response(self, sucsess_text=''):
        return u'<div class = "save_result">%s</div><table>%s</table>\
        <input type="submit" value="Редактировать">' % (sucsess_text,
                                                       self.as_table(),)

    class Meta:
        model = Person
