"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r#n33@()4q+e%n6j8%)c$2o_qpxwy1*-4kt$l$#u6eovmfm-=f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'D:\GlassStar\Charge\logs\logfile.log', 
        },
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['file'],
        #     'level': 'INFO',
        #     'propagate': True,
        # },
        'app': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     'loggers': {
#         # Root logger
#         '': {
#             'handlers': ['file'],  # Add your other handlers here if needed
#             'level': 'INFO',  # Set the desired logging level for this logger
#         },
#         # Your custom logger for 'increase_credit' view
#         'increase_credit_logger': {
#             'handlers': ['increase_credit_file'],
#             'level': 'INFO',  # Set the desired logging level for this logger
#             'propagate': False,  # Avoid propagating logs to the root logger
#         },
#     },

#     'handlers': {
#         # Other handlers...
#         'file': {        
#             'class': 'logging.FileHandler',
#             'filename': 'app.log',  # Set the name and path of the main log file
#             'level': 'INFO',  # Set the desired logging level for the main log file
#         },
#         # Handler for the custom logger
#         'increase_credit_file': {
#             'class': 'logging.FileHandler',
#             'filename': 'increase_credit.log',  # Set the name and path of the custom log file
#             'level': 'INFO',  # Set the desired logging level for the custom log file
#         },
#     },
# }



AUTH_USER_MODEL = 'app.Profile'