from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class  Tree(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.FileField( upload_to='tree/', blank=True, storage=RawMediaCloudinaryStorage())
    image_data = models.BinaryField(null=True)


class Bestimages(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.FileField(upload_to='pics')