from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from profilee.models import Profile



def validate_eight_digits(value):
    if not value.isdigit() or len(value) != 8:
        raise ValidationError('Phone number must be exactly 8 digits.')
    
def validate_past_date(value):
    if value >= timezone.now().date():
        raise ValidationError('Date of birth must be in the past.')


class Complaint(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    COMPLAINT_CHOICES = [
        ('Delayed Orders', 'Delayed Orders'),
        ('Quality Issues', 'Quality Issues'),
        ('Communication Problems', 'Communication Problems'),
        ('Billing and Pricing Disputes', 'Billing and Pricing Disputes'),
        ('Customer Service Issues', 'Customer Service Issues'),
        ('Damaged or Lost Items', 'Damaged or Lost Items'),
        ('Design Issues', 'Design Issues')
    ]
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    ]
    complaint_type = models.CharField(max_length=100, choices=COMPLAINT_CHOICES, null=True, blank=True)
    complaint_text = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint #{self.id} by {self.user_profile.user.username}"