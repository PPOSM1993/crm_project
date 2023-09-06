from django.shortcuts import render, redirect

# Create your views here.
from .forms import *

from django.contrib.auth.models import *
from django.contrib.auth import *

from django.contrib.auth.decorators import *
from .models import *

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
    my_records = Record.objects.all()
    
    context = { 'records': my_records }
    
    return render(request, 'app/dashboard.html', context = context)

login_required(login_url='Login')
def CreateRecords(request):
    
    form = AddRecordForm()
    
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
        
    context = {'form': form}
    
    return render(request, 'app/create-record.html', context = context)

@login_required(login_url='Login')
def UpdateRecords(request, pk):
    
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)
    
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect('Dashboard')
        
    context = {'form': form}
    
    return render(request, 'app/update-record.html', context = context)


@login_required(login_url='Login')

def SingularRecords(request, pk):
    all_records = Record.objects.get(id=pk)
    
    context = {'record': all_records}
    
    return render(request, 'app/view-record.html', context = context)


@login_required(login_url='Login')
def DeleteRecords(request, pk):
    
    record = Record.objects.get(id=pk)
    record.delete()
    
    #messages.success(request, "Your record was deleted!")

    return redirect("Dashboard")

