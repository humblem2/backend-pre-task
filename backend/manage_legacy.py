#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import pymysql
from decouple import config


def install_pymysql_as_mysqldb():
    """
    PyMySQL을 MySQLdb처럼 사용하기 위한 설정
    - PyMySQL이나 MySQLdb는 모두 Mysql DB API 2.0 표준을 따르는 데이터베이스 커넥터 즉 Mysql DB 연동 모듈
    - PyMySQL은 PyMySQL 패키지 설치
    - MySQLdb는 mysqlclient 패키지 설치
    - mysqlclient 패키지, 파이썬 버전 마다 설치 호환 문제 가능성 있음
    - PyMySQL은 MySQLdb보다 속도가 느림
    - MySQLdb가 없으면 PyMySQL을 MySQLdb처럼 사용
    - MySQLdb가 있으면 MySQLdb를 사용
    - MySQLdb가 없고 PyMySQL이 없으면 예외 발생
    - PyMySQL.install_as_MySQLdb()를 호출해야만 Django가 MySQLdb로 인식함
    - settings.py에 DATABASES 설정을 MySQLdb 스타일로 설정 가능
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

