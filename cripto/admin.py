from django.contrib import admin

# Register your models here.
from .models import Key,Uploadfile

class Keyadmin(admin.ModelAdmin):
    list_display= [
            'id',
            'userid',
            'clientId',
            'qu',
            'du',
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
            'cypherwords',
        ]
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Uploadfile,Uploadfileadmin)