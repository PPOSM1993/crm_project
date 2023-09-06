from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=150, verbose_name='First Name', unique=True)
    last_name = models.CharField(max_length=150, verbose_name='Last Name', unique=True)
    email = models.EmailField(
        max_length=150, null=True, blank=True, verbose_name='Email', unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone Number should be +99999999999")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name="Phone Number") # validators 
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Address')
    city = models.CharField(max_length=150, null=True, blank=True, verbose_name='City')
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=125)


    def __str__(self):
        return self.first_name + "   " + self.last_name