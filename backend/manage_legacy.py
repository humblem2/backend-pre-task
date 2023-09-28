#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import pymysql
from decouple import config


def install_pymysql_as_mysqldb():
    """
    PyMySQL을 MySQLdb처럼 사용하기 위한 설정
    """
    pymysql.install_as_MySQLdb()


install_pymysql_as_mysqldb()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

