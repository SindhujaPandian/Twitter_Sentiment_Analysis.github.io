from django.db import models
from django import forms
# Create your models here.

class userModel(models.Model):
    username = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    
