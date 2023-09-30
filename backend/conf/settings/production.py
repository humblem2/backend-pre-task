# production settings
from .base import *

from decouple import Config, RepositoryEnv

env_file = str(BASE_DIR / ".env.development")
config = Config(RepositoryEnv(env_file))

DEBUG = False
ALLOWED_HOSTS = ['production_domain.com', ]

# MySQL Database Connection Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('RDBMS_NAME'),
        'USER': config('RDBMS_USER'),
        'PASSWORD': config('RDBMS_PASSWORD'),
        'HOST': config('RDBMS_HOST'),
        'PORT': config('RDBMS_PORT'),
    }
}

# Managing DDL via SQL
DDL_BY_SQL = False

# Add any other production-specific settings (e.g. cache, multi datasource, storage backends, etc.)
