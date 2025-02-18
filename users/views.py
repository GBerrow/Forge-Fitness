from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm, UserProfileForm
from .models import UserProfile

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'form': form})

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'signup.html', {'form': form})

class ProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class SettingsView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'settings.html'
    fields = ['profile_picture', 'bio']
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_settings'] = self.request.user
        return context

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
