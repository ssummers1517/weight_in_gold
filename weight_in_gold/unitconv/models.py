from django.db import models

# Create your models here.

class ConversionFromPounds(models.Model):
	to = models.CharField(max_length = 20)
	multiplier = models.FloatField()