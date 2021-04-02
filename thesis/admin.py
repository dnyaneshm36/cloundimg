from django.contrib import admin

# Register your models here.
from .models import Senderkey,Receiverkey,Uploaddata


class SenderKeyadmin(admin.ModelAdmin):
    list_display= ['id','socialaccount','sks','pks']
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Senderkey,SenderKeyadmin)

class receiverKeyadmin(admin.ModelAdmin):
    list_display= ['id','socialaccount','sks','pks']
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Receiverkey,receiverKeyadmin)

class Uploaddataadmin(admin.ModelAdmin):
    list_display= ['id','filename','datafile','words']
    # class Meta:
    #     model = Myfrienddetail

admin.site.register(Uploaddata,Uploaddataadmin)