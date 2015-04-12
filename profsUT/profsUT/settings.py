"""
Django settings for profsUT project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6^klb956%pm_2lhg$j%242&-cbq&c)abska6@hdg-yc+@t(7&@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dataCollections',
    'bootstrapform',
    'nested_inline',
    'rest_framework',
    'storages',
    'videos',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'permissions.permissions.ReadOnly',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_jsonp.renderers.JSONPRenderer',
    ),
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'profsUT.urls'

WSGI_APPLICATION = 'profsUT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if False:
    PROJECT_DIR = os.environ['PROJECT_DIR']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

else:
    if 'RDS_DB_NAME' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
        }
        AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
        AWS_ACCESS_KEY_ID = os.environ['S3_ACCESS_KEY_ID']
        AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET_ACCESS_KEY']

        # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
        # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
        # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
        # We also use it in the next setting.
        AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

        # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
        # refers directly to STATIC_URL. So it's safest to always set it.
        

        # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
        # you run `collectstatic`).
        STATICFILES_STORAGE = 's3_storages.custom_storages.StaticStorage'

        STATICFILES_LOCATION = 'static'
        STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

        MEDIAFILES_LOCATION = 'media'
        MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
        DEFAULT_FILE_STORAGE = 's3_storages.custom_storages.MediaStorage'
    else:
        raise Exception("You don't have a database dummy")

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/eb_log/django_log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

VIDEOS_ZENCODER_KEY = os.environ['VIDEOS_ZENCODER_KEY']