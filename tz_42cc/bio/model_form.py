from django.forms import ModelForm
from tz_42cc.bio.models import Person

# Create the form class.
class PersonDetail(ModelForm):           
    class Meta:
        model = Person