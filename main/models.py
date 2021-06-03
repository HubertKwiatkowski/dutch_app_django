from django.db import models
from django.db.models.fields import BooleanField, CharField

class Word(models.Model):
    dutch       = models.CharField(max_length=50)
    het_article = models.BooleanField(default=False)
    de_article  = models.BooleanField(default=False)
    polish      = models.CharField(max_length=50)
    favourite   = models.BooleanField(default=False)
    