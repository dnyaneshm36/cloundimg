from django import forms
from .models import Uploadfile,Key

class UploaddataForm(forms.ModelForm): 
    class Meta:
        model = Uploadfile
        fields = ['datafile','cypherwords']
    # def clean_datafile(self, *args,**kwargs):
        
    #     datafile = self.cleaned_data.get("datafile")
    #     strdata  = str(datafile)
    #     if '.txt'in strdata:
    #         return datafile
    #     else:
    #         raise forms.ValidationError(" Add text formate. ")
    #     return datafile

from django.forms import TextInput
class keysFormid(forms.ModelForm):
    pku1        = forms.CharField(required=False)
    pku2         = forms.CharField(required=False)
    class Meta:
        model = Key
        fields = ['clientId','qu','du']
        widgets = {
            'clientId': TextInput(attrs={'placeholder': 'clientId'}),
             'qu': TextInput(attrs={'placeholder': 'qu'}),
              'du': TextInput(attrs={'placeholder': 'du'}),

        }
class KeyForm(forms.ModelForm):

    class Meta:
        model = Key
        fields = ['clientId','qu','du','pku1','pku2']
        widgets = {
            'clientId': TextInput(attrs={'placeholder': 'clientId'}),
             'qu': TextInput(attrs={'placeholder': 'qu'}),
              'du': TextInput(attrs={'placeholder': 'du'}),

        }

class KeyFormpublic(forms.Form):
    pku1            = forms.CharField(required=False)
    pku2            = forms.CharField(required=False)
    # class Meta:
    #     model = Key
    #     fields = ['pku1','pku2']