from django.contrib import admin
from django.urls import path
from . import views  # Ensure views.py exists

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for a homepage route
]
