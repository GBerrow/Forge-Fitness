from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views
from .forms import LoginForm

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        template_name='login.html',
        authentication_form=LoginForm
    ), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
    
    # Use custom logout view that properly handles session clearing
    path('logout/', views.custom_logout, name='logout'),
    
    # Practice Notes CRUD
    path('notes/create/<str:page>/', views.create_note, name='create_note'),
    path('notes/edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('notes/delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
