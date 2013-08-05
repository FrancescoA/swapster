# Create your views here.
from django.shortcuts import render,get_object_or_404
from trader.models import Trader
from objects.models import Object

def index(request):
	return render(request, 'index.html')



def about_us(request):
	return render(request,'swapster/about_us.html')


def faq(request):
	return render(request, 'swapster/faq.html')