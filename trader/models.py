from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Trader(AbstractUser):
	store_title = models.CharField(max_length=100,default="My Store")
	bio = models.CharField(max_length=500, default="This is a short description of me")
	image = models.ImageField(upload_to="traders/")
	date_created = models.DateTimeField(auto_now=True)



