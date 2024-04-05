from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'auth/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authenticate the user
            user = authenticate(request, username=form.cleaned_data['rollnumber'], password=form.cleaned_data['password'])
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful')
                context = {
                    'name': user.first_name,
                    'user': request.user
                }
                return render(request, 'auth/index.html', context=context)
            else:
                messages.error(request, 'Invalid credentials')
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user or do something with the cleaned_data
            messages.success(request, 'Account created successfully')
            email = form.cleaned_data['email']
            rollnumber = form.cleaned_data['rollnumber']
            password = form.cleaned_data['pass1']
            myuser = User.objects.create_user(rollnumber, email, password)
            myuser.first_name = form.cleaned_data['name']
            myuser.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html', {'form': form})