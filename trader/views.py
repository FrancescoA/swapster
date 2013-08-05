from django.contrib.auth import authenticate, login as auth_login
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from objects.models import Object
from trader.models import Trader, Offer
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
            return redirect('user_profile')
            # Redirect to a success page.
        else:
            messages.add_message(request,messages.INFO, 'Please activate your account before logging in.')
            # Return a 'disabled account' error message
    else:
        messages.add_message(request, messages.ERROR, 'That is an invalid username')
        # Return an 'invalid login' error message.
    return render(request,'registration_form.html')


'''
class TraderDetailView(DetailView):
    model = Trader
    template_name = 'trader/profile.html'

    def get_context_data(self, **kwargs):
        context = super(TraderDetailView, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        try:
            user = Trader.objects.get(username=username)
            items = Object.objects.filter(owner__username=username)
            context['items'] = items
            return context
        except ObjectDoesNotExist:
            messages.add_message(request, messages.ERROR, "User "+username+ " does not exist")
            return redirect('user_profile')

'''

def profile(request, username):
    try:
        user = Trader.objects.get(username=username)
        items = Object.objects.filter(owner__username=username)
        context = {'items' : items,
        'user' : user }
        return render(request, 'trader/profile.html', context)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, "User "+username+ " does not exist")
        return redirect('user_profile')



def tradeview(request,username):
    try:
        other_user = Trader.objects.get(username=username)
        other_items = Object.objects.filter(owner__username=username)
        user = request.user
        items = Object.objects.filter(owner=user)
        context = {
            'other_user' : other_user,
            'other_items' :other_items,
            'user' : user,
            'items' : items
        }
        return render(request, 'trader/trade.html', context)

    except ObjectDoesNotExist: 
        messages.add_message(request, messages.ERROR, "User "+username+ " does not exist")
        return redirect('user_profile')

@csrf_exempt
def makeoffer(request,username):
    try:
        other_user = Trader.objects.get(username=username)
        user = request.user
        offer = Offer()
        offer.maker = user
        offer.receiver = other_user
        offer.save()
        if request.method == 'POST':
            snapmap = request.POST
            print len(snapmap)
            for key in snapmap:
                obj_set = Object.objects.filter(name=key)
                if snapmap[key] == 'in':
                    offer.receiver_objects.add(obj_set.filter(owner=other_user)[0])
                if snapmap[key] == 'out':
                    offer.maker_objects.add(obj_set.filter(owner=user)[0])
            offer.save()
            messages.add_message(request, messages.INFO, "Your offer has been sent")
        return HttpResponse(reverse('user_profile'))

    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, "User "+username+ " does not exist")
        return HttpResponse(reverse('user_profile'))
            

class UpdateTraderView(UpdateView):
    model = Trader
    template_name = 'trader/user_profile.html'
    form_class = TraderForm
    success_url = '/traders/profile'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateTraderView, self).get_context_data(**kwargs)
        items = Object.objects.filter(owner=self.request.user)
        context['items'] = items
        return context

    def form_valid(self, form):
        obj = form.save()
        obj.save()
        messages.add_message(self.request, messages.INFO, "You have successfully edited your profile.")
        return redirect(self.success_url)




