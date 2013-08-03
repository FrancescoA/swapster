from django.forms import ModelForm
from objects.models import Object

class ObjectForm(ModelForm):
	class Meta:
		model = Object
		fields = ('name', 'summary', 'description', 'image')