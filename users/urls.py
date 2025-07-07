from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
    
    # Practice Notes CRUD
    path('notes/create/<str:page>/', views.create_note, name='create_note'),
    path('notes/edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('notes/delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
