"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-qdw2lpoczxap6a4my7j3k-$10@4^8b--$pz07^+c1m(g!c=mbl"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    "src.apps.SrcConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_results",
    "django_celery_beat",
    "rest_framework",
    'corsheaders',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "src.middlewares.authCms.AuthCms",
    "src.middlewares.authClient.AuthClient",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
        "OPTIONS": {
            "init_command": "ALTER DATABASE "
            + os.environ.get("DB_DATABASE", BASE_DIR / "db.sqlite3")
            + " CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci",
        },
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

TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/usr/src/app/static/",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "/cms/auth/login"

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

LOGIN_GOOGLE_CLIENT_ID = os.environ.get("LOGIN_GOOGLE_CLIENT_ID")
LOGIN_GOOGLE_CLIENT_SECRET = os.environ.get("LOGIN_GOOGLE_CLIENT_SECRET")
LOGIN_GOOGLE_REDIRECT = os.environ.get("LOGIN_GOOGLE_REDIRECT")

LOGIN_FACEBOOK_CLIENT_ID = os.environ.get("LOGIN_FACEBOOK_CLIENT_ID")
LOGIN_FACEBOOK_CLIENT_SECRET = os.environ.get("LOGIN_FACEBOOK_CLIENT_SECRET")
LOGIN_FACEBOOK_REDIRECT = os.environ.get("LOGIN_FACEBOOK_REDIRECT")

EMAIL_MAILER = os.environ.get("EMAIL_MAILER", "smtp")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = int(os.environ.get("EMAIL_USE_TLS", True))

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

CELERY_TIMEZONE = "Asia/Ho_Chi_Minh"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "default"
CELERY_BROKER_URL = (
    "redis://default:" + REDIS_PASSWORD + "@" + REDIS_HOST + ":" + REDIS_PORT + "/0"
)
CELERY_BEAT_SCHEDULE = {
    "testSchedule": {
        "task": "src.tasks.testSchedule",
        "schedule": 10.0,
        "args": None,
        "options": {
            "expires": 15.0,
        },
    },
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {asctime}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "log/debug.log",
            "maxBytes": 100000,
            "backupCount": 2,
            "formatter": "verbose",
        },
        "customLog": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "log/customLog.log",
            "maxBytes": 100000,
            "backupCount": 2,
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["logfile"],
            "level": "ERROR",
            "propagate": True,
        },
        "customLog": {
            "handlers": ["customLog"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
