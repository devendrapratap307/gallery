import datetime

from django.db import models


# Create your models here.

class image(models.Model):
    photo = models.ImageField(upload_to="myImageFolder")
    date = models.DateTimeField(auto_now_add=True)  #auto_now_add=True)
