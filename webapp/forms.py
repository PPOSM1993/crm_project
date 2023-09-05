from django.contrib.auth.forms import *
from django.contrib.auth.models import User

from django import forms
#from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import *

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
                        }
                        )
                )

    password = forms.CharField(widget=PasswordInput(attrs={
                            'placeholder': 'Enter Password',
                        }
                    )
                )