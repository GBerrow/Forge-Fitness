from django.urls import path
from . import views

urlpatterns = [
    # Profile Page (Read, Update)
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),

    # Settings Page (Read, Update, Delete)
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/delete/', views.AccountDeleteView.as_view(), name='delete_account'),

    # Login Page (Authenticate)
    path('login/', views.LoginView.as_view(), name='login'),

    # Signup Page (Create User)
    path('signup/', views.SignupView.as_view(), name='signup'),
]