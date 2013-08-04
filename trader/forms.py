from django.forms import ModelForm,Textarea
from trader.models import Trader

class TraderForm(ModelForm):
	class Meta:
		model = Trader
		fields = ('image','first_name', 'last_name', 'bio', 'store_title')
		widgets = {
			'bio' : Textarea(attrs={'rows' : 4}),
		}