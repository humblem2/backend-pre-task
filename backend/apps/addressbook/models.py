from django.conf import settings
from django.db import models
from commons import (
    model_mixins as mx,
)


class Contact(mx.BaseModel, mx.TimeStampedModel):
    """연락처 모델 입니다. 연락처 정보를 저장합니다."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name="유저",
        help_text="이 연락처의 소유자"
    )
    profile_pic = models.URLField(
        blank=True, null=True,
        verbose_name="프로필 사진 URL",
        help_text="연락처의 프로필 사진 URL을 입력하세요."
    )
    name = models.CharField(
        max_length=200,
        verbose_name="이름",
        help_text="연락처의 이름을 입력하세요. (필수 항목)"
    )
    email = models.EmailField(
        blank=True, null=True,
        verbose_name="이메일 주소",
        help_text="연락처의 이메일 주소를 입력하세요."
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="전화번호",
        help_text="연락처의 전화번호를 입력하세요. (필수 항목)"
    )
    company = models.CharField(
        max_length=200, blank=True, null=True,
        verbose_name="소속 회사",
        help_text="연락처의 소속 회사를 입력하세요."
    )
    position = models.CharField(
        max_length=200, blank=True, null=True,
        verbose_name="직책",
        help_text="연락처의 직책을 입력하세요."
    )
    memo = models.TextField(
        blank=True, null=True,
        verbose_name="메모",
        help_text="연락처에 대한 추가 정보나 메모를 입력하세요."
    )
    address = models.TextField(
        blank=True, null=True,
        verbose_name="주소",
        help_text="연락처의 주소를 입력하세요."
    )
    birthday = models.DateField(
        blank=True, null=True,
        verbose_name="생일",
        help_text="연락처의 생일을 입력하세요."
    )
    website = models.URLField(
        blank=True, null=True,
        verbose_name="웹사이트 주소",
        help_text="연락처의 웹사이트 URL을 입력하세요."
    )

    class Meta:
        db_table = 'Contact'
        managed = settings.DDL_BY_SQL
        ordering = ['id']
        verbose_name = "연락처"
        verbose_name_plural = "연락처들"


class Label(mx.BaseModel, mx.TimeStampedModel):
    """라벨 모델 입니다. 라벨 정보를 저장합니다."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='labels',
        verbose_name="유저",
        help_text="이 라벨의 소유자"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="라벨명",
        help_text="라벨의 이름을 입력하세요. (필수 항목)"
    )

    class Meta:
        db_table = 'Label'
        managed = settings.DDL_BY_SQL
        ordering = ['id']
        verbose_name = "라벨"
        verbose_name_plural = "라벨들"


class ContactLabel(mx.BaseModel, mx.TimeStampedModel):
    """연락처-라벨 모델 입니다. 연락처와 라벨의 관계를 매핑하여 저장합니다."""

    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='contactlabel_set',  # labels
        verbose_name="연락처",
        help_text="관련된 연락처를 선택하세요. (필수 항목)"
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name='contactlabel_set',  # contacts
        verbose_name="라벨",
        help_text="관련된 라벨을 선택하세요. (필수 항목)"
    )

    class Meta:
        db_table = 'ContactLabel'
        managed = settings.DDL_BY_SQL
        ordering = ['id']
        unique_together = (('contact', 'label'),)
        verbose_name = '연락처-라벨'
        verbose_name_plural = '(연락처-라벨)들'

    def __str__(self):
        return f"Contact {self.contact.name} <-> Label {self.label.name}"
