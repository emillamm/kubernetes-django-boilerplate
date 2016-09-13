from my_backend.settings.common import *

DEBUG = True

import dj_database_url
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

INSTALLED_APPS += (
    'test_without_migrations',
    )
