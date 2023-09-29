from django.contrib.auth.models import AbstractUser
from django.db import models

from commons import (
    model_mixins as mx,
    constants as c,
)
from django.conf import settings


class User(mx.BaseUserModel, mx.TimeStampedModel, AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name="유저이메일(`로그인 시 아이디`)",
        help_text="이메일을 입력하세요. (필수 항목)"
    )
    username = models.CharField(
        max_length=30, unique=True,
        verbose_name="유저이름",
        help_text="유저의 이름을 입력하세요. (필수 항목)"
    )
    gender = models.CharField(
        max_length=10,
        blank=True,
        choices=c.enum_to_choice(c.Gender),
        default=c.Gender.etc.name,
        verbose_name="성별",
        help_text="성별을 입력하세요. "
    )

    class Meta:
        db_table = 'User'
        managed = settings.DDL_BY_SQL
        ordering = ['id']
        verbose_name = "유저"
        verbose_name_plural = "유저들"
