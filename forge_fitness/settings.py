DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # ✅ Keep it as 'postgresql'
        'NAME': 'forge_fitness',  # ✅ Your PostgreSQL database name
        'USER': 'forge_user',  # ✅ Your PostgreSQL username
        'PASSWORD': 'aberwolves',  # ✅ Your password
        'HOST': '127.0.0.1',  # ✅ Use '127.0.0.1' instead of 'localhost'
        'PORT': '5432',  # ✅ Default PostgreSQL port
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ROOT_URLCONF = 'forge_fitness.urls'
DEBUG = True  


