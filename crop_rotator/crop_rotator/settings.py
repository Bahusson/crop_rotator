"""
Django settings for crop_rotator project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "what_a_supersecret_key_i_see_here_amirite?!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "core.apps.CoreConfig",
    "rotator.apps.RotatorConfig",
    "rekruter.apps.RekruterConfig",
    "strona.apps.StronaConfig",
    "modeltranslation",
    'clearcache',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "login_required",
    # Poniżej dwa typy cleanupu. Zobaczymy, który się sprawdzi,
    # żeby nam bardziej oszczędzić danych.
    # Testowo - manualna (lup przez demona) delecja zdjęć nieużywanych.
    # https://github.com/akolpakov/django-unused-media
    "django_unused_media",
    # "storages", - to chyba cdn - do usunięcia
    # Testowo - autodelecja zdjęć przy usuwaniu wydarzenia.
    # https://github.com/un1t/django-cleanup
    "django_cleanup.apps.CleanupConfig",
]

# Kolejność tego draństwa jest ważna.
# https://docs.djangoproject.com/en/2.2/topics/cache/#order-of-middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "login_required.middleware.LoginRequiredMiddleware",
]

ROOT_URLCONF = "crop_rotator.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "crop_rotator.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mygenericdb",
        "USER": "postgres",
        "PASSWORD": "super_duper_password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# AUTH_USER_MODEL = "rekruter.User"
# Używamy uproszczonego modelu usera, bo nie chcemy się ładować w rodo.

# CACHE bazodanowy. https://docs.djangoproject.com/en/2.2/topics/cache/
# Przed użyciem stwórz tabelę w bazie danych za pomocą:
# "python manage.py createcachetable"
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache_table",
        "TIMEOUT": 1,  # Ustaw więcej w produkcji. Obczaj źródło na górze.
        "OPTIONS": {"MAX_ENTRIES": 2000, "CULL_FREQUENCY": 2},
    }
}

CACHE_MIDDLEWARE_ALIAS = "default"

CACHE_MIDDLEWARE_SECONDS = 1

CACHE_MIDDLEWARE_KEY_PREFIX = ""

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# Dla sesji opartych na ciastkach:
# "django.contrib.sessions.backends.signed_cookies"
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "pl"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Moduł tłumaczeniowy, jak wszystko z MODELTRANSLATION w nazwie
# https://django-modeltranslation.readthedocs.io/en/latest/
# klasy są tak poustawiane, że dodanie lub usunięcie języka z settings.py
# automatycznie powoduje ich dodanie/usunięcie wszędzie indziej.
# TODO: Poprawić langjs.js żeby też był z tym zsynchronizowany.
gettext = lambda s: s
LANGUAGES = (
    ("pl", gettext("Polish")),
    ("en", gettext("English")),
)

LANGUAGE_COOKIE_AGE = 31449600  # Około rok ważności ciacha w sekundach.
# Ustaw None jeśli chcesz, żeby się zerowały po każdym wyłączeniu przeglądarki.

LANGUAGE_COOKIE_NAME = "rotator_language"  # Nazwa ciacha językowego.

LANGUAGE_COOKIE_PATH = "/"  # Domyślna ścieżka ciastków.

MODELTRANSLATION_DEFAULT_LANGUAGE = "pl"  # Tu możesz zmienić default language.

MODELTRANSLATION_LANGUAGES = (
    "pl",
    "en",
)

# W ten sposób zachowają sie języki jak nie znajdzie się jakiegoś w bazie.
MODELTRANSLATION_FALLBACK_LANGUAGES = {"default": ("en", "pl")}

# Tutaj rejestruje się wszystkie trackery translacyjne translation.py
MODELTRANSLATION_TRANSLATION_FILES = (
    # "rotator.translation",
    "strona.translation",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, "crop_rotator/static")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "/"  # Przekierowanie usera po zalogowaniu

LOGOUT_REDIRECT_URL = "/"  # Przekierowanie po wylogowaniu.

# Poniżej dane do ustawień Middleware blokującego strony przed niezalogowanymi.
LOGIN_URL = "/"

# https://github.com/CleitonDeLima/django-login-required-middleware
LOGIN_REQUIRED_IGNORE_PATHS = [
    r"^$",
    r"^strona/.*$",
    r"^rekruter/logger/$",
    r"^rekruter/register/$",
    r"^static/.*$",
    r"^media/.*$",
    r"^admin/.*$",
]

# Ściągnij ustawienia lokalne gdybyśmy chcieli udostępnić kod i wejść na OpenSource
# na serwerze obok "settings" robisz plik .local_settings i ustalasz od nowa:
# SECRET_KEY, DEBUG = False, DATABASES, oraz CACHES jeśli używasz Memccache.
# edit: oraz inne o których było wspomniane wcześniej.
try:
    from .local_settings import *
except ImportError:
    pass
