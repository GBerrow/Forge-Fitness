from django.shortcuts import render

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
