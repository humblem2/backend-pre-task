from .development import *

from decouple import Config, RepositoryEnv
from manage import install_pymysql_as_mysqldb

# Managing DDL via SQL
DDL_BY_SQL = True

# Use PyMySQL as the default-adaptor for MySQL in Django
env_file = str(BASE_DIR / ".env.development")
config = Config(RepositoryEnv(env_file))
DEFAULT_DB_ADAPTOR_CHANGE = bool(config('DJANGO_USE_PYMYSQL_AS_MYSQLDB', default='False'))
if DEFAULT_DB_ADAPTOR_CHANGE:
    install_pymysql_as_mysqldb()
