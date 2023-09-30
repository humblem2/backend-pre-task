from rest_framework import serializers

from apps.addressbook import (
    models as m,
)
from commons import (
    serializer_mixins as sm,
)


class ContactLabelSerializer(sm.BaseModelSerializer):
    """ContactLabel 모델의 생성, 삭제 시 사용"""

    class Meta:
        model = m.ContactLabel
        fields = ('id', 'contact', 'label')
        ref_name = "ContactLabel"
