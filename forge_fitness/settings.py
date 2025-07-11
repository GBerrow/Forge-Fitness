import os
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

# Allowed Hosts (force it to be set)
allowed_hosts_env = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1,testserver")
ALLOWED_HOSTS = allowed_hosts_env.split(",")

# Session settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Authentication settings
LOGIN_URL = '/login/'  
LOGIN_REDIRECT_URL = '/'  
LOGOUT_REDIRECT_URL = '/login/'

# Custom authentication backend to allow login with either username or email
AUTHENTICATION_BACKENDS = [
    'users.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',  # Keep as fallback
]

# Session backend
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Database configuration - SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
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

# Static file settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'forge_fitness' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Authentication settings
LOGIN_URL = '/login/'  
LOGIN_REDIRECT_URL = '/'  
LOGOUT_REDIRECT_URL = '/login/'

# Security settings (disabled for local development)
if DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True