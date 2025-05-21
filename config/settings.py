import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # This should point to DJANGO-REACT-SAMPLE

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-super-secret-django-key-goes-here' # CHANGE THIS!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Set to False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # Add your production domain(s) here

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # For serving static files
    'rest_framework',         # For Django REST Framework
    'api.apps.ApiConfig',     # YOUR API APP - CRUCIAL FOR DYNAMIC ROUTING
    # 'corsheaders',            # If you need more complex CORS than Vite proxy provides
    # Add any other Django apps here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # For serving static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware', # If using corsheaders
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls' # Points to your main urls.py file

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # This tells Django where to find the React app's index.html after it's built
        'DIRS': [os.path.join(BASE_DIR, 'app', 'dist')],
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

WSGI_APPLICATION = 'config.wsgi.application' # For WSGI servers like Gunicorn

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# If you have a custom user model in 'api/models/user.py' and it's named 'User'
# AUTH_USER_MODEL = 'api.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'

# This is where Django's 'collectstatic' will gather all static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# This tells Django where to look for additional static files (your React app's built assets)
# Vite typically puts built assets into an 'assets' subfolder within the 'dist' directory.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app', 'dist', 'assets'),
]

# For WhiteNoise (serving static files efficiently in production)
# Ensure 'whitenoise.middleware.WhiteNoiseMiddleware' is high in MIDDLEWARE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional: Django REST Framework settings
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.SessionAuthentication',
#         # Add other authentication methods if needed
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
#     ),
# }

# Optional: CORS Headers settings if you use the 'corsheaders' app
# and aren't relying solely on Vite's proxy for development.
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173", # Your Vite frontend dev server
#     "http://127.0.0.1:5173",
# ]
# CORS_ALLOW_CREDENTIALS = True # If you need to send cookies across domains