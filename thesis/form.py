from django.forms import ModelForm
from .models import Uploaddata

class UploaddataForm(ModelForm):
    class Meta:
        model = Uploaddata
        fields = ['filename','datafile','words']
