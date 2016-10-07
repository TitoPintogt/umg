from __future__ import unicode_literals

from django.db import models

from app.municipio.models import Municipio

# Create your models here.
	
class Aldea(models.Model):
	municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
    
