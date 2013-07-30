from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

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
            return render(request, "index.html")
            # Redirect to a success page.
        else:
            messages.add_message(request,message.INFO, 'Please activate your account before logging in.')
            # Return a 'disabled account' error message
    else:
        messages.add_message(request, message.ERROR, 'That is an invalid username')
        # Return an 'invalid login' error message.
    return render(request,'registration_form.html')