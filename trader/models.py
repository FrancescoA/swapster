from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Trader(AbstractUser):
	store_title = models.CharField(max_length=100)
	
