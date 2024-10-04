"""
Django settings for playground project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from django.conf.global_settings import MEDIA_ROOT, STATIC_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-v0n9(!pwhu7qhcv%xp5t3sve&hor$7!5x&dtb=s)x^t@=wb%25"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    "custom_admin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_group_model",
    "corsheaders",
    "djmoney",
    "django_filters",
    "constance",
    "accounts",
    "laptops",
    "payment",
    'ckeditor',
  'ckeditor_uploader'
]

# CUSTOM GROUP MODEL
AUTH_USER_MODEL = 'accounts.Employee'
AUTH_GROUP_MODEL = 'accounts.Group'


#
CORS_ORIGIN_ALLOW_ALL = True
# Does not match any trusted origin error
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']

# Paypal
CLIENT_ID = "AfM2JMozc5j_fAO20lOoG0tIepszxOLenWlhnaaJ318_x3cIx3pYjd3DdoEUsXikRKfm5iFhSXS-0yTX"
APP_SECRET = "ED9LTPDFA8bNOXmVC-GxbjYfu0_sTEifTY5YcILX7jCG3urCSymNbRrtStd3QdusdJTRsH_2DU8bNe1O"
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'

CONSTANCE_CONFIG = {
    'SESSION_TIMEOUT_SECONDS': (5, 'Answer to the Ultimate Question of Life, '
                       'The Universe, and Everything'),
}

def get_constance(name: str) -> object:
    return CONSTANCE_CONFIG[name][0]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "playground.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [os.path.join(BASE_DIR, '../admin/templates')],
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "playground.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "/"

LANGUAGE_CODE = 'en-us'

USE_I18N = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
}

CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'