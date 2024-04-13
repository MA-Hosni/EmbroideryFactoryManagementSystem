from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



def validate_eight_digits(value):
    if not value.isdigit() or len(value) != 8:
        raise ValidationError('Phone number must be exactly 8 digits.')
    
def validate_four_digits(value):
    if not value.isdigit() or len(value) != 4:
        raise ValidationError('Matricule must be exactly 4 digits.')
    
def validate_past_date(value):
    if value >= timezone.now().date():
        raise ValidationError('Date of birth must be in the past.')

# Create your models here.
class Adherent(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    email = models.EmailField(null=True)
    date_de_naissance = models.DateField(
        null=True,
        validators=[validate_past_date]
    )
    cin = models.CharField(
        max_length=8,
        validators=[validate_eight_digits],
        unique=True,
    )
    phone_number = models.CharField(
        max_length=8,
        validators=[validate_eight_digits],
        unique=True,
    )
    adress = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'adherent {self.id}: {self.first_name} {self.last_name}'
# Create your models here.
class Employee(models.Model):
  first_name = models.CharField(max_length=20, null=True)
  last_name = models.CharField(max_length=20, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  matricule = models.CharField(
        max_length=4,
        validators=[validate_four_digits],
        unique=True,  
    )
  admin = models.BooleanField(default=False)
  email = models.EmailField(null=True)
  date_de_naissance = models.DateField(
        null=True,
        validators=[validate_past_date]
    )
  cin = models.CharField(
        max_length=8,
        validators=[validate_eight_digits],
        unique=True,  
    )
  phone_number = models.CharField(
        max_length=8,
        validators=[validate_eight_digits],
        unique=True,  
    )
  adress = models.CharField(max_length=100, null=True)
  ville = models.CharField(max_length=30, null=True)
  departement = models.CharField(max_length=30, null=True)

  def __str__(self):
    return f'Employee {self.id}: {self.first_name} {self.last_name}'
# Create your models here.
class Intern(models.Model):
  first_name = models.CharField(max_length=20, null=True)
  last_name = models.CharField(max_length=20, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  email = models.EmailField(null=True)
  date_de_naissance = models.DateField(
        null=True,
        validators=[validate_past_date]
    )
  cin = models.CharField(
        max_length=8,
        validators=[validate_eight_digits],
        unique=True,  
    )
  phone_number = models.CharField(
        max_length=8,
        validators=[validate_eight_digits],
        unique=True,  
    )
  faculte = models.CharField(max_length=50, null=True)
  specialite = models.CharField(max_length=30, null=True)
  departement = models.CharField(max_length=30, null=True)
  encadrant = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='supervised_interns'
    )

  def __str__(self):
      return f'Intern {self.id}: {self.first_name} {self.last_name}'
