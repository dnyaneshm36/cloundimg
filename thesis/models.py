from django.db import models
from django.conf import settings
# Create your models here.

from allauth.socialaccount.models import SocialAccount
# Create your models here.
# from cloudinary.models import CloudinaryField
# from cloudinary_storage.storage import RawMediaCloudinaryStorage

# the uid given by the social account like google is smaller than Q so
# we can use it as client secrete .
class Senderkey(models.Model):
    socialaccount =                      models.ForeignKey(SocialAccount,on_delete=models.CASCADE)
    clientsecrete =                      models.CharField(max_length=50,default=None)
    sks           =                      models.CharField(max_length=500)
    pks           =                      models.CharField(max_length=500)




class Receiverkey(models.Model):
    socialaccount =                      models.ForeignKey(SocialAccount,on_delete=models.CASCADE)
    clientsecrete =                      models.CharField(max_length=50,default=None)
    sks           =                      models.CharField(max_length=500)
    pks           =                      models.CharField(max_length=500)


class Uploaddata(models.Model):
    filename     =                       models.CharField(max_length=100)
    datafile     =                       models.FileField(null = True,upload_to='files/')
    words        =                       models.CharField(max_length=1000)