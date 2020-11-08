from django.db import models
from django.db.models.base import Model

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)