from django.contrib.auth.forms import *
from django.contrib.auth.models import User

from django import forms
#from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import *
from .models import *
#Register/Create user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

#Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={
                            'placeholder': 'Enter Username',
                            'class': 'form form-control form-control-sm'
                        }
                        )
                )
    password = forms.CharField(widget=PasswordInput(attrs={
                            'placeholder': 'Enter Password',
                            'class': 'form form-control form-control-sm'
                        }
                    )
                )

class AddRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = '__all__'
    
    first_name = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter First Name',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )
    
    last_name = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter Last Name',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )

    email = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter Email',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )

    phone = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter Phone Number',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )


    address = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter Address',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )

    city = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter City',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )

    province = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter City',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )

    country = forms.CharField(
        widget=TextInput(attrs={
            'placeholder': 'Enter Country',
            'class': 'form form-control form-control-sm text-uppercase'
            }
        )
    )


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'