from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import *
from profilee.models import Profile
from .forms import ComplaintForm
from login.decorators import *
from notification.models import Notification


# Create your views here.
#page submit complaint
@login_required(login_url='loginpage')
def subcomplaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            # Set the user_profile to the logged-in user's profile
            complaint = form.save(commit=False)
            complaint.user_profile = request.user.profile  # Assuming the profile is linked to the user model
            complaint.save()
            return redirect('followcomplaint')  # Redirect to a success page or complaint list page
    else:
        form = ComplaintForm()
    
    context = {'form': form, 'notifications': Notification.objects.all()}
    return render(request, 'frontclient/complaintsubmit.html', context)

#page follow complaint
@login_required(login_url='loginpage')
def follcomplaint(request):
    profile = Profile.objects.get(user=request.user)
    user_complaints = Complaint.objects.filter(user_profile=profile)

    return render(request, 'frontclient/followcomplaint.html', {'complaints': user_complaints, 'notifications': Notification.objects.all()})