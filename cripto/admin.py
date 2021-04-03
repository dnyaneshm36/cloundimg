from django.contrib import admin

# Register your models here.
from .models import Key

class Keyadmin(admin.ModelAdmin):
    list_display= [
            'id',
            'socialaccount',
            'clientId',
            'qu',
            'du',
            'su',
            'sku1',
            'sku2',
            'pku1',
            'pku2'
        ]
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Key,Keyadmin)