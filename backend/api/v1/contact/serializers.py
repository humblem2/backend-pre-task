from rest_framework import serializers

from api.v1 import (
    validators as v
)
from api.v1.label import (
    serializers as ls,
)
from apps.addressbook import (
    models as m,
)
from commons import (
    serializer_mixins as sm,
)


class ContactListSerializer(sm.BaseModelSerializer):
    """Contact모델 목록 조회 시 사용"""

    phone_number = serializers.CharField(validators=[v.is_valid_phone_number])
    labels = serializers.SerializerMethodField(help_text="연락처에 매핑된 라벨의 리스트입니다.")

    class Meta:
        model = m.Contact
        fields = ('id', 'profile_pic', 'name', 'email', 'phone_number',
                  'company', 'position', 'labels', 'created_at', 'updated_at')
        ref_name = "Contact - (List)"

    def get_labels(self, obj):
        """@overide 연락처 모델 조회 시 라벨 정보도 같이 나오도록 재정의한 메서드"""

        labels = m.Label.objects.filter(contactlabel_set__contact=obj)
        return ls.LabelSerializer(labels, many=True).data


class ContactDetailSerializer(serializers.ModelSerializer):
    """Contact모델 상세, 수정, 생성 시 사용"""

    phone_number = serializers.CharField(validators=[v.is_valid_phone_number])
    labels = serializers.SerializerMethodField()

    class Meta:
        model = m.Contact
        fields = ('id', 'profile_pic', 'name', 'email', 'phone_number',
                  'company', 'position', 'memo', 'labels', 'address',
                  'birthday', 'website', 'created_at', 'updated_at')
        ref_name = 'Contact - (Detail)'

    def get_labels(self, obj):
        labels = m.Label.objects.filter(contactlabel_set__contact=obj)
        return ls.LabelSerializer(labels, many=True).data

    def create(self, validated_data):
        """역직렬화시 user 필드가 필수(FK) 필드이므로, user 정보 추가 후 생성"""
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
