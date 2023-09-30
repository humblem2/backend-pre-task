"""
conftest.py
이 파일은 테스트 코드에서 매개변수로 주입하여 사용하는 공통 Custom-fixture를 정의합니다.
"""
from typing import List

import pytest
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.addressbook.models import Contact, Label, ContactLabel

User = get_user_model()


@pytest.fixture
def test_user() -> User:
    """User를 생성하여 반환"""
    return get_user_model().objects.create_user(
        username="testuser",
        email="test@test.com",
        password="testpass123"
    )


@pytest.fixture
def authenticated_api_client(test_user: User) -> APIClient:
    """JWT 인증을 사용하는 API 클라이언트"""
    client = APIClient()
    refresh = RefreshToken.for_user(test_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def api_client() -> APIClient:
    """인증 없는 API 클라이언트"""
    return APIClient()


@pytest.fixture
def authenticated_api_request(test_user: User, authenticated_api_client: APIClient) -> HttpRequest:
    """JWT 인증을 사용하는 API 클라이언트 픽스처를 HttpRequest 객체로 변환하고 User를 추가하여 반환"""
    request = authenticated_api_client.request()
    request.user = test_user
    return request


@pytest.fixture
def test_contact_of_user(test_user: User) -> Contact:
    """인증된 사용자의 Contact 생성하여 반환"""
    return Contact.objects.create(user=test_user, name="testcontactuser", email="humblem2@naver.com", phone_number="010-1111-2222")


@pytest.fixture
def test_label_of_user(test_user: User) -> Label:
    """인증된 사용자의 Label 생성하여 반환"""
    return Label.objects.create(user=test_user, name="testlabel")


@pytest.fixture
def test_contact_label(test_contact_of_user: Contact, test_label_of_user: Label) -> ContactLabel:
    """인증된 사용자의 ContactLabel 생성하여 반환"""
    return ContactLabel.objects.create(contact=test_contact_of_user, label=test_label_of_user)


@pytest.fixture
def test_labels_of_user(test_user: User, test_contact_of_user: Contact) -> List[Label]:
    """인증된 사용자의 Label 여러 개(2EA) `생성`하고 특정 Contact와 `연결`하여 반환"""

    label1: Label = Label.objects.create(user=test_user, name="testlabel-1")
    label2: Label = Label.objects.create(user=test_user, name="testlabel-2")

    ContactLabel.objects.create(contact=test_contact_of_user, label=label1)
    ContactLabel.objects.create(contact=test_contact_of_user, label=label2)

    return [label1, label2]
