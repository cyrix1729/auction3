from pathlib import Path
import os.path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

CORS_ALLOW_CREDENTIALS = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6neq52l=s9!*i0ugbazd5l+gnazpp%sai9o($(6advzaj__#ln"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:5173', 'http://localhost:5173']

INSTALLED_APPS = [
    "django_crontab",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "auctionApp",

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


ROOT_URLCONF = "auction.urls"

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
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

WSGI_APPLICATION = "auction.wsgi.application"


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

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL="auctionApp.User"
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
MEDIA_ROOT = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SERVER_EMAIL = 'newdjangobay@gmail.com'
DEFAULT_FROM_EMAIL = 'newdjangobay@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'newdjangobay@gmail.com'
EMAIL_HOST_PASSWORD = 'skcstlovwefjbvcb'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#CRONJOBS = [('* * * * *', 'auctionApp.cron.my_cron_job')]
