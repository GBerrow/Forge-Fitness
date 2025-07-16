from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from users.views import SignupView, CustomLoginView, custom_logout
from django.views.decorators.cache import never_cache
from . import views

# Decorator that combines login_required and never_cache
def protected_view(view_func):
    return never_cache(login_required(view_func))

urlpatterns = [
    # Root URL - redirects to dashboard
    path('', RedirectView.as_view(url='/dashboard/', permanent=False), name='home'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Main app pages (protected with cache prevention)
    path('dashboard/', protected_view(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    path('activity/', protected_view(views.activity), name='activity'),
    path('training/', protected_view(TemplateView.as_view(template_name='training.html')), name='training'),
    path('progression/', protected_view(TemplateView.as_view(template_name='progression.html')), name='progression'),
    
    # Auth pages (public)
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    
    # User-specific URLs
    path('', include('users.urls')),
]

# Static and media files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)