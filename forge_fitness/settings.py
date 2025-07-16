import os
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

# Load .env file
load_dotenv()

# Get the base directory of the project dynamically
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (force it to be set)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("❌ Missing DJANGO_SECRET_KEY environment variable")

# Debug mode (defaults to False for security)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# FIXED: Allowed Hosts for Render
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
if os.getenv('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS.append(os.getenv('RENDER_EXTERNAL_HOSTNAME'))

# Enhanced Session settings for security
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_SAVE_EVERY_REQUEST = False  # Changed from True - this was causing issues
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # or your preferred backend
SESSION_COOKIE_SECURE = True if not DEBUG else False
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True if not DEBUG else False
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection

# Authentication settings
LOGIN_URL = '/login/'  
LOGIN_REDIRECT_URL = '/dashboard/'  # Changed from '/' to '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

# Custom authentication backend to allow login with either username or email
AUTHENTICATION_BACKENDS = [
    'users.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',  # Keep as fallback
]

# FIXED: Database configuration for Render (PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

ROOT_URLCONF = 'forge_fitness.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Installed Django apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

AUTH_USER_MODEL = 'users.UserProfile'

# FIXED: Middleware with WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'users.middleware.SessionSecurityMiddleware',  # Add this line
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'forge_fitness' / 'templates',
            BASE_DIR / 'users' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# FIXED: Static file settings for Render
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'forge_fitness' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise settings for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security settings
if DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Additional production security
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Custom error handlers (works even in DEBUG mode)
handler404 = 'users.views.custom_404_view'
handler500 = 'users.views.custom_500_view'