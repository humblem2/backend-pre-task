#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from typing import Dict

import pymysql
from decouple import Config, config, RepositoryEnv
from termcolor import colored

from conf.settings.base import BASE_DIR


def load_environment() -> Dict[str, str]:
    """환경변수 파일(`.env`)을 기반으로 배포환경을 고려한 Django 설정 모듈을 로드합니다."""

    # 배포환경에 따라 환경변수 파일 선택
    environment = config('ENVIRONMENT', default='development')
    env_file = f'.env.{environment}'
    selected_env_file = str(BASE_DIR / env_file)

    # 선택한 환경변수 파일로부터 설정 로드
    custom_config = Config(RepositoryEnv(selected_env_file))
    django_settings_module = custom_config('DJANGO_SETTINGS_MODULE', default='conf.settings.development')

    return {
        'environment': environment,
        'selected_env_file': selected_env_file,
        'django_settings_module': django_settings_module
    }


def pretty_print_colored(**kwargs):
    """중요 정보 색상화하여 출력"""
    box_width = 70
    print(colored("┌" + "─"*(box_width-2) + "┐", 'yellow'))
    for key, value in kwargs.items():
        formatted_key = key.replace("_", " ").capitalize()  # 'selected_env_file' -> 'Selected env file'
        key_width = len(formatted_key) + 2
        print(colored(f"│ {formatted_key}: {value:<{box_width - key_width - 2}}│", 'green'))
    print(colored("└" + "─"*(box_width-2) + "┘", 'yellow'))


def install_pymysql_as_mysqldb():
    """PyMySQL을 MySQLdb처럼 사용하기 위한 설정"""
    pymysql.install_as_MySQLdb()


def main():
    """Run administrative tasks."""
    install_pymysql_as_mysqldb()
    environment_data = load_environment()
    django_settings_module = environment_data['django_settings_module']
    pretty_print_colored(**environment_data)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)
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
