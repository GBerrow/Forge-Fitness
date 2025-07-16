from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
    
    # Remove the logout URL from here since it's in main urls.py
    # path('logout/', views.custom_logout, name='logout'),
    
    # Practice Notes CRUD
    path('notes/create/<str:page>/', views.create_note, name='create_note'),
    path('notes/edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('notes/delete/<int:note_id>/', views.delete_note, name='delete_note'),
    
    # Test error pages (REMOVE THESE AFTER TESTING)
    path('test-404/', views.test_404_error, name='test_404'),
    path('test-500/', views.test_500_error, name='test_500'),
    path('preview-404/', views.custom_404_view, name='preview_404'),
    path('preview-500/', views.custom_500_view, name='preview_500'),
]
