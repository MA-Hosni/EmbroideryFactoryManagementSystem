from .models import *
from profilee.models import *
from django import forms

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_type', 'complaint_text']
        widgets = {
            'complaint_text': forms.Textarea(attrs={'id': 'description', 'maxlength': '1000'}),
        }
