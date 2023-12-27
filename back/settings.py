"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from datetime import timedelta
# from firebase_admin import credentials, storage
# import firebase_admin
from pathlib import Path
import os

import pyrebase


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ...

# Firebase Configuration
FIREBASE_CREDENTIALS_FILE = os.path.join(BASE_DIR, './firebase_credentials.json')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x-4=o#*khj=1pj7=+p&ftg-)t*lb*jd9bk47tr42o9^=+lfq@1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '.vercel.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'poate',
    "corsheaders",
    'multiselectfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ALLOWED_HOSTS=['http://localhost:3000', 'localhost']               

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
       'http://localhost:3000',
)

ROOT_URLCONF = 'back.urls'

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

WSGI_APPLICATION = 'back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

FIREBASE_CONFIG = {
  "apiKey": "AIzaSyAKfSqnFESmoyi7uh6139wDYZioBB20ANg",
  "authDomain": "django-2546a.firebaseapp.com",
  "databaseURL": "https://django-2546a-default-rtdb.firebaseio.com",
  "projectId": "django-2546a",
  "storageBucket": "django-2546a.appspot.com",
  "messagingSenderId": "507483439501",
  "appId": "1:507483439501:web:40104306f954f53490bdc4",
  "measurementId": "G-TE8316F38Y"
}

# cred = credentials.Certificate(FIREBASE_CREDENTIALS_FILE)
# firebase_admin.initialize_app(cred, {"databaseURL":"https://django-2546a-default-rtdb.firebaseio.com"}, name="image_upload_app")

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()
auth_pyre = firebase.auth()
