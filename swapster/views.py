# Create your views here.
from django.shortcuts import render,get_object_or_404
from trader.models import Trader
from objects.models import Object

def index(request):
	print Object.objects.all()
	print request.user.object_set.all()
	return render(request, 'swapster/profile.html')