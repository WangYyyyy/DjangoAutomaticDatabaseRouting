from django.db import models

# Create your models here.
class App1Model(models.Model):
	line1 = models.CharField(max_length=50)
	line2 = models.CharField(max_length=50)
	line3 = models.IntegerField()

# 定义settings中的DATABASE_APPS_MAPPING的APPname 可忽略
class Meta:
	app_label = "app1"