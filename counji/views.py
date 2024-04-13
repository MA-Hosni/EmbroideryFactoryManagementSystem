from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import *
from profilee.models import Profile
from .forms import *
from login.decorators import *
from notification.models import Notification


# Create your views here.
#page submit complaint
@login_required(login_url='loginpage')
def subconge(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            employee = Employe.objects.get(user_employee=request.user.profile)  # Retrieve the Employee instance
            leave_request.user_profile = employee
            leave_request.save()
            return redirect('followcounji')  # Redirect to a success page or leave requests list page
    else:
        form = LeaveRequestForm()

    context = {'form': form, 'notifications': Notification.objects.all()}
    return render(request, 'frontclient/counjisubmit.html', context)

#page follow complaint
@login_required(login_url='loginpage')
def follconge(request):
    # Get the logged-in employee's profile
    employee_profile = request.user.profile

    # Filter leave requests related to the employee's profile
    leave_requests = Counji.objects.filter(user_profile__user_employee__user=employee_profile.user)
    # Get the employee associated with the profile
    employee = Employe.objects.get(user_employee=employee_profile)

    context = {'leave_requests': leave_requests, 'employee': employee, 'notifications': Notification.objects.all()}
    return render(request, 'frontclient/followcounji.html', context)
