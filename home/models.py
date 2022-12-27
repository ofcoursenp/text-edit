from django.db import models

# Create your models here.

class Text(models.Model):
    text = models.CharField(max_length=99999999)
    newtext = models.CharField(max_length=99999999)
    
    def __str__(self):
        return self.text


