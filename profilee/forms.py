from django import forms
from django.contrib.auth.models import User
from .models import Profile, Code

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'cin', 'phone_number', 'state']  
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class CodeForm(forms.ModelForm):
    number = forms.CharField()
    class Meta:
        model = Code
        fields = ['number']