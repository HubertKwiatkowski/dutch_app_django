from django.db import models


class Word(models.Model):
    polish      = models.CharField(max_length=50)
    dutch       = models.CharField(max_length=50)
    het_article = models.BooleanField(default=False)
    de_article  = models.BooleanField(default=False)
    favourite   = models.BooleanField(default=False)
    

    def __str__(self):
        return self.polish