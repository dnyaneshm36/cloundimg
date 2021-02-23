from django.forms import ModelForm
from .models import Tree


class UploadImageForm(ModelForm):
    class Meta:
        model = Tree
        fields = ['name','image','desc']
