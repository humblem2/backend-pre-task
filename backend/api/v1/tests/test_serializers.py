"""
test_serializers.py

이 파일은 `api/v1/` 디렉토리의 `serializer.py` 에 대한 테스트를 담고 있습니다.
- serializer의 직렬화/역직렬화
"""
from typing import List

import pytest
from django.http import HttpRequest
from rest_framework.exceptions import ValidationError

from api.v1.contact.serializers import ContactListSerializer, ContactDetailSerializer
from api.v1.contact_label.serializers import ContactLabelSerializer
from api.v1.label.serializers import LabelSerializer, LabelUpdateSerializer
from apps.addressbook.models import Contact, Label, ContactLabel


@pytest.mark.django_db
class TestContactSerializer:

    def test_contact_serializer(self, test_contact_of_user: Contact):
        """ContactListSerializer의 `labels` 필드 없이 Lazy-loading 하게 연락처 정보 조회 직렬화 검증"""
        serializer = ContactListSerializer(test_contact_of_user)
        data = serializer.data

        assert data["name"] == "testcontactuser"
        assert data["email"] == "humblem2@naver.com"
        assert data["phone_number"] == "010-1111-2222"

    def test_contact_serializer_with_labels(self, test_contact_of_user: Contact, test_labels_of_user: List[Label]):
        """ContactListSerializer의 연락처과 연결된 라벨리스트 직렬화 검증"""
        serializer = ContactListSerializer(test_contact_of_user)
        data = serializer.data

        assert data["name"] == "testcontactuser"
        assert data["email"] == "humblem2@naver.com"
        assert data["phone_number"] == "010-1111-2222"

        serialized_labels = data["labels"]  # labels 필드
        assert len(serialized_labels) == 2

        expected_labels = ["testlabel-1", "testlabel-2"]
        for i, label_data in enumerate(serialized_labels):
            assert label_data["name"] == expected_labels[i]


@pytest.mark.django_db
class TestContactDetailSerializer:

    def test_contact_detail_serializer_data(self, test_contact_of_user: Contact, test_label_of_user: Label):
        """
        ContactDetailSerializer의 연락처과 연결된 라벨리스트 직렬화 검증
        """

        # 연락처에 라벨 연결
        ContactLabel.objects.create(contact=test_contact_of_user, label=test_label_of_user)

        serializer = ContactDetailSerializer(test_contact_of_user)
        data = serializer.data

        # 필수필드 검증
        assert data["name"] == "testcontactuser"
        assert data["email"] == "humblem2@naver.com"
        assert data["phone_number"] == "010-1111-2222"

        # 라벨필드 검증
        serialized_labels = data["labels"]
        assert len(serialized_labels) == 1

        label_serializer = LabelSerializer(test_label_of_user)
        assert serialized_labels[0] == label_serializer.data

    def test_contact_detail_serializer_validation(self):
        """
        ContactDetailSerializer의 필드 중 [이메일,..] 필드의 유효성 검사 기능을 검증
        """
        invalid_data = {
            "name": "testcontactuser",
            "email": "humblem2@naver.com",
            "phone_number": "01011112222",  # 형식 불일치
        }

        serializer = ContactDetailSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert "phone_number" in serializer.errors

    def test_contact_detail_serializer_deserialization(self, test_user, authenticated_api_request: HttpRequest):
        """
        ContactDetailSerializer의 역직렬화 검증. 생성, 상세, 수정 기능에 사용하는 시리얼라이저.
        """
        valid_data = {
            "name": "newcontact",
            "email": "humblem2@naver.com",
            "phone_number": "010-1234-5678",
            "user": test_user.id,
        }

        serializer = ContactDetailSerializer(data=valid_data, context={'request': authenticated_api_request})

        assert serializer.is_valid()

        new_contact = serializer.save()
        assert new_contact.name == "newcontact"
        assert new_contact.email == "humblem2@naver.com"
        assert new_contact.phone_number == "010-1234-5678"


@pytest.mark.django_db
class TestLabeSerializer:

    def test_label_serializer(self, test_label_of_user: Label):
        """LabelSerializer이 라벨 직렬화 검증"""
        serializer = LabelSerializer(test_label_of_user)
        data = serializer.data

        assert data["name"] == "testlabel"


@pytest.mark.django_db
class TestContactLabelSerializer:
    def test_contact_label_serializer(self, test_contact_label: ContactLabel):
        """ContactLabelSerializer 직렬화 검증"""
        serializer = ContactLabelSerializer(test_contact_label)
        data = serializer.data

        assert data["contact"] == test_contact_label.contact.id
        assert data["label"] == test_contact_label.label.id


@pytest.mark.django_db
class TestLabelUpdateSerializer:

    def test_label_update_serializer_serialization(self, test_label_of_user):
        """LabelUpdateSerializer 직렬화 검증"""
        serializer = LabelUpdateSerializer(test_label_of_user)
        data = serializer.data

        assert data["name"] == "testlabel"
        assert "id" not in data  # id 필드는 제외

    def test_label_update_serializer_deserialization(self, test_label_of_user):
        """LabelUpdateSerializer 역직렬화 및 유효성 검사 기능 검증"""
        new_name = "NewLabelName"
        serialized_data = {"name": new_name}
        serializer = LabelUpdateSerializer(instance=test_label_of_user, data=serialized_data)

        # 유효성 검사
        assert serializer.is_valid()

        # 데이터 업데이트
        updated_label = serializer.save()

        # 변경된 이름 확인
        assert updated_label.name == new_name
        assert updated_label.name != "testlabel"

    def test_label_update_serializer_invalid_data(self):
        """LabelUpdateSerializer의 유효성 검사 검증"""
        serialized_data = {"name": ""}
        serializer = LabelUpdateSerializer(data=serialized_data)

        # 유효성 검사 시 ValidationError가 발생하여 실패한다면 테스트 통과 판단
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
