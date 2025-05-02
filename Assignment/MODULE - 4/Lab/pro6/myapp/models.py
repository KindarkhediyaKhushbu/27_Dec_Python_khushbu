from django.db import models
from.models import *

# Create your models here.
class doctors(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    specialty = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='doctorphoto')
    degree = models.CharField(max_length=30)
    bio = models.TextField()