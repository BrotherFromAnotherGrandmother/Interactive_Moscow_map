from django import forms
from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.TextField()
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates = models.JSONField()

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
