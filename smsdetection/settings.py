"""
Django settings for smsdetection project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
'''
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2-%06rt1g*sp66(3@#-8a)kjae1usf@6b40733se56(ubnj&=u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['your-render-domain.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'detection',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smsdetection.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'smsdetection.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''
# Import Path from pathlib for handling file paths
from pathlib import Path

# Set the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent
import os

# Define templates directory path
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Secret key for cryptographic signing - WARNING: Should be kept secret in production
SECRET_KEY = 'django-insecure-2-%06rt1g*sp66(3@#-8a)kjae1usf@6b40733se56(ubnj&=u'

# Debug mode - Should be False in production
DEBUG = False

# Allowed hosts list - Empty means only localhost is allowed
ALLOWED_HOSTS = ['SMS-SPAM-DETECTION.onrender.com']

# Installed Django apps
INSTALLED_APPS = [
    # Django's built-in apps
    'django.contrib.admin',      # Admin interface
    'django.contrib.auth',       # Authentication system
    'django.contrib.contenttypes',# Content type system
    'django.contrib.sessions',   # Session framework
    'django.contrib.messages',   # Messaging framework
    'django.contrib.staticfiles',# Static file management
    'detection',                # Our custom SMS detection app
]

# Middleware - Components that process requests/responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # Security
    'whitenoise.middleware.WhiteNoiseMiddleware',       # WhiteNoise for serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',   # Session handling
    'django.middleware.common.CommonMiddleware',             # Common features
    'django.middleware.csrf.CsrfViewMiddleware',             # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',# Authentication
    'django.contrib.messages.middleware.MessageMiddleware',   # Messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking protection
]

# Root URL configuration
ROOT_URLCONF = 'smsdetection.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # Directory containing our templates
        'APP_DIRS': True,         # Look for templates in app directories
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

# WSGI application path
WSGI_APPLICATION = 'smsdetection.wsgi.application'

# Database configuration - Using SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    # Various password validators for security
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'    # Default language
TIME_ZONE = 'UTC'          # Time zone
USE_I18N = True           # Internationalization
USE_TZ = True            # Time zone support

# Static files configuration
STATIC_URL = 'static/'    # URL to use when referring to static files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'