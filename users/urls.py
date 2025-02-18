# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/delete/', views.AccountDeleteView.as_view(), name='delete_account'),
    path('login/', views.LoginView.as_view(), name='login'),  # Changed from log-in
    path('signup/', views.SignupView.as_view(), name='signup'),  # Changed from sign-up
]
