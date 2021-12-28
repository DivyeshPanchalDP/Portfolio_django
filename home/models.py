from django.db import models

# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=255)
    companyname = models.CharField(max_length=255)
    email = models.CharField(max_length=35)
    info = models.TextField()
  
