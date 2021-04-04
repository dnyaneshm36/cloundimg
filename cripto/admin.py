from django.contrib import admin

# Register your models here.
from .models import Key,Uploadfile

class Keyadmin(admin.ModelAdmin):
    list_display= [
            'id',
            'userid',
            'clientId',
            'su',
            'sku1',
            'qu',
            'du',
            'sku2',
            'pku1',
            'pku2'
        ]
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Key,Keyadmin)

class Uploadfileadmin(admin.ModelAdmin):
    list_display= [
            'id',
            'userid',
            'datafile',
            'words',
        ]
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Uploadfile,Uploadfileadmin)