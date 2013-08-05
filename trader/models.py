from django.db import models
from django.contrib.auth.models import AbstractUser
from objects.models import Object
from swapster import settings
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


class Offer(models.Model):
	maker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='made_offer')
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_offer')
	message = models.TextField(default="Would you be interested in trading with me?")
	maker_objects = models.ManyToManyField(Object, related_name='trade')
	receiver_objects = models.ManyToManyField(Object, related_name='want')

	def accept(self):
		if self.maker == self.receiver:
			self.delete()
		for item in self.maker_objects.all():
			item.owner = self.receiver
			item.save()

		for item in self.receiver_objects.all():
			item.owner = self.maker
			item.save()
		
		self.delete()

