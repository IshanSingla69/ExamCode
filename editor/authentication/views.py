from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import CustomUser

def home(request):
    return render(request, 'auth/login.html')

def login(request):
    if request.user.is_authenticated:
        if request.user.account_type == 'student':
            return redirect('student:student_dashboard')
        elif request.user.account_type == 'teacher':
            return redirect('makeTest:create_test')
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        if user is not None:
            auth_login(request, user)
            request.session['name'] = user.first_name
            if user.account_type == 'student':
                return redirect('student:student_dashboard')
            elif user.account_type == 'teacher':
                return redirect('makeTest:create_test')
            return redirect('authentication:home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('authentication:home')
    return render(request, 'auth/login.html')

def logout(request):
    auth_logout(request)
    # messages.success(request, 'Logged out successfully')
    return redirect('authentication:home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            email = form.cleaned_data['email']
            rollnumber = form.cleaned_data['rollnumber']
            password = form.cleaned_data['pass1']
            account_type = form.cleaned_data['account_type']
            myuser = CustomUser.objects.create_user(rollnumber, email, password, account_type=account_type)
            myuser.first_name = form.cleaned_data['name']
            myuser.save()
            return redirect('authentication:login')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html', {'form': form})

def instructions(request):
    return render(request,'homepage/instructions.html')
def about(request):
    return render(request,'homepage/about.html')