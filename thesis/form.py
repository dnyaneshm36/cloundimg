from django import forms
from .models import Uploaddata

class UploaddataForm(forms.ModelForm):
    datafile        = forms.FileField()
    class Meta:
        model = Uploaddata
        fields = ['filename','datafile','words']
    def clean_datafile(self, *args,**kwargs):
        
        datafile = self.cleaned_data.get("datafile")
        strdata  = str(datafile)
        if '.txt'in strdata:
            return datafile
        else:
            raise forms.ValidationError(" Add text formate. ")
        return datafile