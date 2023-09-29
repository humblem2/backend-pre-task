from rest_framework import serializers

from apps.addressbook import (
    models as m,
)
from commons import (
    serializer_mixins as sm,
)


class LabelSerializer(sm.BaseModelSerializer):
    """Label 모델의 조회 시 사용"""

    class Meta:
        model = m.Label
        fields = ['id', 'name']
        ref_name = 'Label'


class LabelUpdateSerializer(serializers.ModelSerializer):
    """Label 모델 상세, 수정, 생성 시 사용"""

    class Meta:
        model = m.Label
        fields = ['name']
        ref_name = 'Label (Update Only)'
