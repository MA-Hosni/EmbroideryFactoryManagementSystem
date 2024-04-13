from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random


def validate_phone_number_with_country_code(value):
    # Remove spaces and plus sign from the value
    cleaned_value = value.replace(" ", "").replace("+", "")

    # Check if the cleaned value contains only digits and has a minimum length of 8
    if not cleaned_value.isdigit() or len(cleaned_value) < 8:
        raise ValidationError('Invalid phone number format.')

def validate_eight_digits(value):
    if not value.isdigit() or len(value) != 8:
        raise ValidationError('Phone number must be exactly 8 digits.')
    
def validate_past_date(value):
    if value >= timezone.now().date():
        raise ValidationError('Date of birth must be in the past.')

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        null=True,
        validators=[validate_past_date]
    )
    cin = models.CharField(
          max_length=8,
          validators=[validate_eight_digits],
          unique=True,
          blank=True,  
    )
    phone_number = models.CharField(
          max_length=12,
          validators=[validate_phone_number_with_country_code],
          unique=True,
          blank=True,  
    )
    STATES_CHOICES = [
        ('Ariana', 'Ariana'),
        ('Béja', 'Béja'),
        ('Ben Arous', 'Ben Arous'),
        ('Bizerte', 'Bizerte'),
        ('Gafsa', 'Gafsa'),
        ('Gabès', 'Gabès'),
        ('Jendouba', 'Jendouba'),
        ('Kairouan', 'Kairouan'),
        ('Kasserine', 'Kasserine'),
        ('Kef', 'Kef'),
        ('Kebili', 'Kebili'),
        ('Mahdia', 'Mahdia'),
        ('Manouba', 'Manouba'),
        ('Medenine', 'Medenine'),
        ('Monastir', 'Monastir'),
        ('Nabeul', 'Nabeul'),
        ('Siliana', 'Siliana'),
        ('Sidi Bouzid', 'Sidi Bouzid'),
        ('Sousse', 'Sousse'),
        ('Sfax', 'Sfax'),
        ('Tataouine', 'Tataouine'),
        ('Tozeur', 'Tozeur'),
        ('Tunis', 'Tunis'),
        ('Zaghouan', 'Zaghouan'),
    ]
    state = models.CharField(max_length=20, choices=STATES_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    

class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
    
    def save(self, *args, **kwargs):
        number_list = [0,1,2,3,4,5,6,7,8,9]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args, **kwargs)