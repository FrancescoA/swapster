# Create your views here.
from django.shortcuts import render,get_object_or_404
from trader.models import Trader

def index(request):
	return render(request, 'swapster/profile.html')