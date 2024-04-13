from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from login.decorators import *
from notification.models import Notification

# Create your views here.
# @admin_only
@login_required(login_url='loginpage')
def dashboard(request):
    return render(request, 'frontend/dashboard.html', {'notifications': Notification.objects.all()})