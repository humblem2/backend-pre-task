# development settings
from decouple import Config, RepositoryEnv

from .base import *

env_file = str(BASE_DIR / ".env.development")
config = Config(RepositoryEnv(env_file))

DEBUG = True
ALLOWED_HOSTS = []

# MySQL Database Connection Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Supported engines: 'postgresql', 'mysql', 'sqlite3', 'oracle', 'djongo'
        'NAME': config('RDBMS_NAME'),
        'USER': config('RDBMS_USER'),
        'PASSWORD': config('RDBMS_PASSWORD'),
        'HOST': config('RDBMS_HOST'),
        'PORT': config('RDBMS_PORT'),
        'TEST': {
            'NAME': config('TEST_RDBMS_NAME'),  # unittest db
        },
    }
}

INSTALLED_APPS += ['drf_yasg', 'debug_toolbar', 'django_extensions', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INTERNAL_IPS = ['127.0.0.1', ]

# Managing DDL via SQL
DDL_BY_SQL = False
