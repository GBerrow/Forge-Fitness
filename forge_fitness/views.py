from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

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

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

# Authentication Views
def custom_logout(request):
    logout(request)
    return redirect('dashboard')  