# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to homepage
    else:
        form = AuthenticationForm()
    return render(request, 'log-in.html', {'form': form})  # Fixed path


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to homepage
    else:
        form = UserCreationForm()
    return render(request, 'sign-up.html', {'form': form})  # Fixed path

def logout_view(request):
    """Logs out the user and redirects to the homepage"""
    logout(request)
    return redirect('dashboard')  # Redirect to homepage

