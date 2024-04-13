from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import Adherent, Employee, Intern
from .forms import InternForm
from login.decorators import *
from notification.models import Notification


# Create your views here.
#page adherent
@login_required(login_url='loginpage')
def adherents(request):
    return render(request, 'frontend/adherents.html', {
        'atherents': Adherent.objects.all(), 'notifications': Notification.objects.all()
    })
#page employee
@login_required(login_url='loginpage')
def employees(request):
    return render(request, 'frontend/employees.html', {
        'employees': Employee.objects.all(), 'notifications': Notification.objects.all()
    })
#page stagieres
@login_required(login_url='loginpage')
def interns(request):
    return render(request, 'frontend/interns.html', {
        'interns': Intern.objects.all(), 'notifications': Notification.objects.all()
    })
# def view_adherent(request, id):
#     adherent = Adherent.objects.get(pk=id)
#     return HttpResponseRedirect(reverse('adherent'))
# delete adherent
def delete_adherent(request, id):
    adherent = Adherent.objects.get(pk=id)
    adherent.delete()
    return HttpResponseRedirect(reverse('adherent'))
# delete employee
def delete_employee(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return HttpResponseRedirect(reverse('employees'))
# delete stagiere
def delete_intern(request, id):
    intern = Intern.objects.get(pk=id)
    intern.delete()
    return HttpResponseRedirect(reverse('interns'))
# add stagiere
def add(request):
    if request.method == 'POST':
        form = InternForm(request.POST)
        if form.is_valid():
            new_intern = form.save()  # Create and save the new Intern instance
            return render(request, 'frontend/addintern.html', {
                'form': InternForm(),
                'success': True
            })
    else:
        form = InternForm()
        employees = Employee.objects.all()
        form.fields['encadrant'].choices = [(employee.id, f'{employee.first_name} {employee.last_name}') for employee in employees]
    return render(request, 'frontend/addintern.html', {
        'form': InternForm()
    })

