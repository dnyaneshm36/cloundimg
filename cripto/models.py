from django.db import models


from allauth.socialaccount.models import SocialAccount

# Create your models here.

class Key(models.Model):
    socialaccount =                      models.ForeignKey(SocialAccount,on_delete=models.CASCADE)
    clientId      =                      models.CharField(max_length=50,default=None)
    qu            =                      models.CharField(max_length=300)
    du            =                      models.CharField(max_length=300)
    su            =                      models.CharField(max_length=100)
    sku1          =                      models.CharField(max_length=100)
    sku2          =                      models.CharField(max_length=300)
    pku1          =                      models.CharField(max_length=300)
    pku2          =                      models.CharField(max_length=300) 