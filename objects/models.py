from django.db import models

# Create your models here.


class Object(models.Model):
	name = models.CharField(max_length=30)
	