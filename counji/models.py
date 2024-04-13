from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from profilee.models import Profile



def validate_eight_digits(value):
    if not value.isdigit() or len(value) != 8:
        raise ValidationError('Phone number must be exactly 8 digits.')
    
def validate_four_digits(value):
    if not value.isdigit() or len(value) != 4:
        raise ValidationError('Matricule must be exactly 4 digits.')
     
def validate_past_date(value):
    if value >= timezone.now().date():
        raise ValidationError('Date of birth must be in the past.')

def validate_future_date(value):
    if value < timezone.now().date():
        raise ValidationError('Date of birth must be in the future.')


class Employe(models.Model):
    user_employee = models.OneToOneField(Profile, on_delete=models.CASCADE)
    matricule = models.CharField(
        max_length=4,
        validators=[validate_four_digits],
        unique=True,  
    )
    departement = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return f'Employee {self.id}: {self.user_employee.user.first_name} {self.user_employee.user.last_name}'

class Counji(models.Model):
    user_profile = models.ForeignKey(Employe, on_delete=models.CASCADE)
    LEAVE_CHOICES = [
        ('Vacation', 'Vacation'),
        ('Sick Leave', 'Sick Leave'),
        ('Personal Leave', 'Personal Leave'),
        ('Maternity Leave', 'Maternity Leave'),
        ('Paternity Leave', 'Paternity Leave'),
        ('Bereavement Leave', 'Bereavement Leave'),
        ('Unpaid Leave', 'Unpaid Leave'),
        ('Jury Duty Leave', 'Jury Duty Leave'),
    ]
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    ]
    start_date = models.DateField()
    end_date = models.DateField()
    resumption_date = models.DateField()
    leave_type = models.CharField(max_length=100, choices=LEAVE_CHOICES, null=True, blank=True)
    reason_for_leave = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leave #{self.id} by {self.user_profile.user_employee.user.username}"