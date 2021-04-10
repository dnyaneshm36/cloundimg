from django.db import models
from django.conf import settings
# Create your models here.
class Key(models.Model):
    userid        =                             models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    clientId      =                      models.CharField(max_length=50,default=None)
    qu            =                      models.CharField(max_length=300)
    du            =                      models.CharField(max_length=300)
    pku1          =                      models.CharField(max_length=300,null=True)
    pku2          =                      models.CharField(max_length=300,null=True) 

class Uploadfile(models.Model):
    userid          =                       models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    datafile        =                       models.FileField(null = True,upload_to='cripto/')
    cypherwords     =                       models.TextField(max_length=10000,null=True)