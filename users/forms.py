from django import forms
from .models import Intern, Employee


class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ['first_name', 'last_name', 'email', 'date_de_naissance', 'cin', 'phone_number', 'faculte', 'specialite', 'departement', 'encadrant']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'date_de_naissance': 'Birth Date',
            'cin': 'CIN',
            'phone_number': 'Phone Number',
            'faculte': 'University',
            'specialite': 'Task Field',
            'departement': 'Department',
            'encadrant': 'Supervisor'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_de_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cin': forms.NumberInput(attrs={'class': 'form-control', 'max': '99999999'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'max': '99999999'}),
            'faculte': forms.TextInput(attrs={'class': 'form-control'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control'}),
            'departement': forms.TextInput(attrs={'class': 'form-control'}),
            'encadrant': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(InternForm, self).__init__(*args, **kwargs)

        # Populate the choices for 'encadrant' field with employees' first names and last names
        employees = Employee.objects.all()
        encadrant_choices = [(employee.id, f'{employee.first_name} {employee.last_name}') for employee in employees]
        self.fields['encadrant'].choices = encadrant_choices