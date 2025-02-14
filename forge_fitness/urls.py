from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('activity/', views.activity, name='activity'),
    path('training/', views.training, name='training'),
    path('progression/', views.progression, name='progression'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
