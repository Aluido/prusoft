from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Receta(models.Model):
	titulo = models.CharField(max_length=100)
	detalle = models.TextField()
	ingredientes = models.TextField()
	imagen = models.ImageField(upload_to='upload/')

	def __str__(self):
		return self.titulo
	
	def detalleProcessor(self):
		return "\n-".join(self.detalle.split('-'))