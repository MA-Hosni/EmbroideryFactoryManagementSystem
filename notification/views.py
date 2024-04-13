from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Notification



@login_required(login_url='loginpage')
def follownotification(request):
    notifications = Notification.objects.all()
    return render(request, 'frontend/notification.html', {'notifications': notifications})

@login_required(login_url='loginpage')
def notificationclient(request):
    notifications = Notification.objects.all()
    return render(request, 'frontend/notificationclient.html', {'notifications': notifications})