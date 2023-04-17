from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacts(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    countery_code = models.CharField(max_length=30)
    phone_number= models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_img = models.ImageField(null=True)
    is_favorite = models.BooleanField(default=False)
