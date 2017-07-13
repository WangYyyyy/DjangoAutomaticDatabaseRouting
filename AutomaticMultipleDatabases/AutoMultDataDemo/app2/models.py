from django.db import models

# Create your models here.
class App2Model(models.Model):
	line1 = models.CharField(max_length=50)
	line2 = models.CharField(max_length=50)
	line3 = models.IntegerField()
