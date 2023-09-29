from django.db import models


class BaseUserModel:
    def __str__(self):
        return f"{self.username}"


class BaseModel:
    def __str__(self):
        return f"{self.name}"


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성일시",
        help_text="생성시 자동 생성"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="수정일시",
        help_text="수정시 자동 갱신"
    )

    class Meta:
        abstract = True
