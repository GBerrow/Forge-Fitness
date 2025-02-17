from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Page Views
def dashboard(request):
    return render(request, 'dashboard.html')

def activity(request):
    return render(request, 'activity.html')

def training(request):
    return render(request, 'training.html')

def progression(request):
    return render(request, 'progression.html')

def settings(request):
    return render(request, 'settings.html')

def profile(request):
    return render(request, 'profile.html')

# Authentication Views
def login(request):
    return render(request, 'users/log-in.html')

def signup(request):
    return render(request, 'users/sign-up.html')

def custom_logout(request):
    logout(request)
    return redirect('dashboard')  
