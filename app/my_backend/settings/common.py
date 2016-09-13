from __future__ import absolute_import

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = os.environ.get('SECRET_KEY', '1234')
HOST = os.environ.get('HOST')
DATABASE_URL = ''
try:
    # If database username, password, host and dbname is set, use those
    postgres_host_env_name = os.environ['POSTGRES_HOST_ENV_NAME']
    postgres_host = os.environ[postgres_host_env_name]
    postgres_db = os.environ['POSTGRES_DB']
    postgres_user = os.environ['POSTGRES_USER']
    postgres_password = os.environ['POSTGRES_PASSWORD']
    DATABASE_URL = 'postgis://%s:%s@%s/%s' % (
        postgres_user, postgres_password, postgres_host, postgres_db)
except Exception:
    # Default to DATABASE_URL fake path.
    # Necessary if running collectstatic without a database
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgis://:@/')

FRONTEND_URL = os.environ.get('FRONTEND_URL')
DEBUG = (os.getenv('DEBUG', '') == 'true')
# Detect if testing

TESTING = False
try:
    TESTING = sys.argv[1:2] == ['test']
except Exception, e:
    pass
if TESTING:
    CELERY_ALWAYS_EAGER = True
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

# POSTGIS_VERSION evn var must be in the following format:
# '2 1' for postgis version 2.1 or '2 1 2' for postgis version 2.1.2
POSTGIS_VERSION = tuple(
    map(int, os.environ.get('POSTGIS_VERSION', '2 2 2').split(' ')))

# define in deployment-specific file
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    # pre-installed Django packages
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    # third-party packages
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'django_extensions',
    'markdownx',

    # our apps
    'my_backend.apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'my_backend.middleware.crossdomainxhr.XsSharing',
)

ROOT_URLCONF = 'my_backend.urls'
WSGI_APPLICATION = 'my_backend.wsgi.application'

# Define in deployment-specific file
DATABASES = {
    'default': {
    }
}

AUTHENTICATION_BACKENDS = (
    # this is default
    'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

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

# Celery and Rabbit MQ
# Set BROKER_URL from either BROKER_HOST_ENV_NAME or CELERY_BROKER_URL
BROKER_URL = ''
try:
    broker_host_env_name = os.environ['BROKER_HOST_ENV_NAME']
    broker_host = os.environ[broker_host_env_name]
    BROKER_URL = 'amqp://guest:@%s:5672//' % broker_host
except Exception:
    BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = 'amqp'
CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.