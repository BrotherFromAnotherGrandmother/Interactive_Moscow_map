from django import forms
from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.TextField()
    # img = models.ImageField()
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.JSONField()
