from django.forms import ModelForm, Textarea
from models import Person
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
import settings

# Create the form class.
class PersonForm(ModelForm):   
    birthdate = forms.DateField(widget=AdminDateWidget())
    
    def __init__(self, *args, **kw): 
        super(ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()       
    
    class Meta:
        model = Person
        js = ('/admin/jsi18n/',
              settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/forms.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/base.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',)
        }
        widgets = {
            'contacts': Textarea(attrs={'cols': 40, 'rows': 2}),
        }