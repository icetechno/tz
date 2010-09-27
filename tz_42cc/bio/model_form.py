from django.forms import ModelForm, Textarea, DateField
from models import Person
from django.forms.extras.widgets import SelectDateWidget

# Create the form class.
class PersonForm(ModelForm):
    birthdate = DateField(widget=SelectDateWidget())
    def __init__(self, *args, **kw): 
        super(ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder.reverse()
        
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