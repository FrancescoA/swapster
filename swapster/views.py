# Create your views here.
from django.shortcuts import render,get_object_or_404
from trader.models import Trader
from objects.models import Object

def index(request):
	items = Object.objects.filter(owner=request.user)
	return render(request, 'swapster/profile.html', {'items' : items})