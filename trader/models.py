from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Trader(AbstractUser):
	store_title = models.CharField(max_length=100,default="My Store")
	bio = models.CharField(max_length=500, default="This is a short description of me")
	image = models.ImageField(upload_to="traders/")
	date_created = models.DateTimeField(auto_now=True)

	def image_url(self):
		if self.image:
			return self.image.url
		else:
			return "http://s7.postimg.org/5q3jk5cm3/default.jpg"

