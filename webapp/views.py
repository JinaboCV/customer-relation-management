from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record

# HomePage


def home(request):
    return render(request, 'webapp/index.html')

# Register 
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}    
    return render(request, 'webapp/register.html' , context=context)        

# Login a user 

def my_login(request):
    form  = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            # checking if the user exists
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)

# Logout
 
def user_logout(request):
    auth.logout(request)
    return redirect('login')

# Create a record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    context = {"records": records}
    return render(request, 'webapp/dashboard.html', context=context)