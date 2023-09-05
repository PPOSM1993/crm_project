from django.shortcuts import render, redirect

# Create your views here.
from .forms import *

from django.contrib.auth.models import *
from django.contrib.auth import *

from django.contrib.auth.decorators import *

def Home(request):
    
    return render(request, 'app/index.html')

# Register User
def Register(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')

    context = { 'form': form }

    return render(request, 'app/register.html', context=context)

#Login User

def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                
                return redirect('Dashboard')
    
    context = {'form': form}
    
    return render(request, 'app/my-login.html', context=context)

#logout user
def LogoutUser(request):
    auth.logout(request)
    
    return redirect("Login")


#Dashboard
@login_required(login_url='Login')
def Dashboard(request):
    return render(request, 'app/dashboard.html')