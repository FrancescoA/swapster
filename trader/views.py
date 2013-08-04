from django.contrib.auth import authenticate, login as auth_login
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from objects.models import Object
from trader.models import Trader
from trader.forms import TraderForm


def login(request):
    print request.POST
    username = request.POST['username']
    password = request.POST['password']
    print username
    print password
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            messages.add_message(request,messages.SUCCESS, 'You have successfully logged in!')
            return redirect('trader.views.profile')
            # Redirect to a success page.
        else:
            messages.add_message(request,message.INFO, 'Please activate your account before logging in.')
            # Return a 'disabled account' error message
    else:
        messages.add_message(request, message.ERROR, 'That is an invalid username')
        # Return an 'invalid login' error message.
    return render(request,'registration_form.html')


def profile(request):
    items = Object.objects.filter(owner=request.user)
    context = {'items' : items}
    return render(request, 'trader/user_profile.html', context)



class UpdateTraderView(UpdateView):
    model = Trader
    template_name = 'trader/edit_profile.html'
    form_class = TraderForm

    def get_object(self, queryset=None):
        return self.request.user

#def trader_profile(request):



