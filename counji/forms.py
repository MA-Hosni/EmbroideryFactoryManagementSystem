from django import forms
from .models import *
from profilee.models import *

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = Counji
        fields = ['start_date', 'end_date', 'resumption_date', 'leave_type', 'reason_for_leave']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'resumption_date': forms.DateInput(attrs={'type': 'date'}),
        }
