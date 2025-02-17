# forge_fitness/urls.py
from django.contrib import admin
from django.urls import path, include
from forge_fitness import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('activity/', views.activity, name='activity'),
    path('training/', views.training, name='training'),
    path('progression/', views.progression, name='progression'),
    path('settings/', views.settings, name='settings'),
    
    # Users (login and signup only)
    path('users/', include('users.urls')),
    
    # Direct Logout Route (Inline for simplicity)
    path('logout/', views.custom_logout, name='logout'),
]
