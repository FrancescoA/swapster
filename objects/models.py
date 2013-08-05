from django.db import models
from django.conf import settings

# Create your models here.


class Object(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="item")
	name = models.CharField(max_length=30)
	summary = models.CharField(max_length=500)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to="objects/")
	date_created = models.DateTimeField(auto_now=True)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

	def date_createdToString(self):
		format = "%m/%d/%Y" 
		return self.date_created.strftime(format)