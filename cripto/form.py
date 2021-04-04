from django import forms
from .models import Uploadfile,Key

class UploaddataForm(forms.ModelForm):
    # datafile        = forms.FileField()
    class Meta:
        model = Uploadfile
        fields = ['datafile','words']
    # def clean_datafile(self, *args,**kwargs):
        
    #     datafile = self.cleaned_data.get("datafile")
    #     strdata  = str(datafile)
    #     if '.txt'in strdata:
    #         return datafile
    #     else:
    #         raise forms.ValidationError(" Add text formate. ")
    #     return datafile


class keysForm(forms.ModelForm):
    # datafile        = forms.FileField()
    class Meta:
        model = Key
        fields = ['clientId','su','sku1','qu','du','sku2','pku1','pku2']