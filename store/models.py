from django.db import models

class Clothes(models.Model):
	description = models.CharField(max_length=64)
	manufacturer = models.CharField(max_length=64)
	gender = models.CharField(max_length=64)
	quantity = models.IntegerField()
	price = models.FloatField()
	size = models.IntegerField()
	picture = models.ImageField()


		
		
