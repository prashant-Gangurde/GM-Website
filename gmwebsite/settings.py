"""
Django settings for gmwebsite project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zwlu1@m&t71k6zbm0=pzfvx9q(*&5lk681z35+za9!bcd)qije'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
EXTERNAL_APPS =['home']
INSTALLED_APPS += EXTERNAL_APPS

# MIDDLEWARE = [
# 'django.middleware.security.SecurityMiddleware',
# 'whitenoise.middleware.WhiteNoiseMiddleware',
# # other middleware


# ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Added for sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Added for authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Added for messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'gmwebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'gmwebsite.wsgi.application'


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

# STATIC_URL = 'static/'
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATIC_URL = "/static/"
# STATIC_ROOT = BASE_DIR / "staticfiles"



# STATICFILES_DIRS = [BASE_DIR / "static"]
# DEBUG = False
# ALLOWED_HOSTS = ['https://gm-website-2bvl01wla-swatii1436s-projects.vercel.app', 'localhost']



# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# For production use with WhiteNoise to serve static files efficiently
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Define the root directory for static files (used by collectstatic)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Directories where Django will search for additional static files
STATICFILES_DIRS = [BASE_DIR / "static"]

# Set DEBUG to True only in development
DEBUG = True  # Set to True in development

# Hostnames allowed to serve your Django app (add your domain and localhost)
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost', 
    'gm-website-44qh-calvnnmng-swatii1436s-projects.vercel.app'
]




# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
