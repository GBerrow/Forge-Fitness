from django.contrib import admin
from django.urls import path, include
from forge_fitness import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('activity/', views.activity, name='activity'),
    path('training/', views.training, name='training'),
    path('progression/', views.progression, name='progression'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth
    path('', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)