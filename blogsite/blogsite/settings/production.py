from .base import *
from .env import SECRET_KEY

DEBUG = False
#DEBUG = True

STATIC_ROOT = '/home/gregwag/wagfront.com/public/static'

MEDIA_ROOT = '/home/gregwag/wagfront.com/public/media'

try:
    from .local import *
except ImportError:
    pass

try:
    from .env import SECRET_KEY
except ImportError:
    pass

ALLOWED_HOSTS = ['.wagfront.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#COMPRESS_OFFLINE = True
#LIBSASS_OUTPUT_STYLE = 'compressed'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
