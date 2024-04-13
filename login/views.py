from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import *
from profilee.forms import CodeForm
from profilee.models import *


# Create your views here.
@unauthenticated_user
def welcome(request):
    return render(request, 'acceuil.html')

# Create your views here LOGIN.
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verifyview')
        else:
            messages.info(request, 'Username or Password incorrect. Please try again!')

    context = {}
    return render(request, 'login.html', context)

# Create your views here LOGOUT.
def logoutUser(request):
    logout(request)
    return redirect('loginpage')

def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user_profile = Profile.objects.get(user_id=pk)
        code = user_profile.code.number
        code_user = f"{user_profile.user.username}: {code}"
        if not request.POST:
            print(code_user)
            # send sms
        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                login(request, user_profile.user)  # Use user_profile.user to access the User object
                return redirect('dashboard')
            else:
                return redirect('loginpage')
    return render(request, 'otp.html', {'form': form})
