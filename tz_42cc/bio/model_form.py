from django.forms import ModelForm, Textarea
from models import Person

# Create the form class.
class PersonDetail(ModelForm):           
    class Meta:
        model = Person
        widgets = {
            'contacts': Textarea(attrs={'cols': 40, 'rows': 2}),
        }