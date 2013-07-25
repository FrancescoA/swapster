from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Trader(AbstractUser):
	store_title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="traders/")
	date_created = models.DateTimeField(auto_now=True)



