from my_backend.settings.common import *

DEBUG = False

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'www', 'media')

# explicitly set host name of server here
# Use * for now. Change to a real host later.
ALLOWED_HOSTS = ['*']

import dj_database_url
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

# disable browsable UI in production
_DEFAULT_RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
)
try:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = _DEFAULT_RENDERER_CLASSES
except NameError:
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': _DEFAULT_RENDERER_CLASSES
    }