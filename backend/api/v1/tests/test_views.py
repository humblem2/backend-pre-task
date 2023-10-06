"""
test_views.py

이 파일은 `api/v1/` 디렉토리의 `views.py` 파일에 대한 테스트를 담고 있습니다.
"""
from typing import List

import jwt
import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.addressbook.models import Contact, Label, ContactLabel

User = get_user_model()


@pytest.mark.django_db
class TestAuthentication:
    def test_register(self):
        client = APIClient()
        response = client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password': 'newpassword123'
        })
        assert response.status_code == 201
        assert response.data['username'] == 'newuser'
        assert response.data['email'] == 'newuser@test.com'

    def test_login(self, test_user: User):
        client = APIClient()
        response = client.post(reverse('login'), {
            'email': test_user.email,
            'password': 'testpass123'
        })

        # Django 설정에서 SECRET_KEY 가져오기
        secret_key = settings.SECRET_KEY

        # API에서 반환된 토큰의 페이로드를 디코드
        returned_payload = jwt.decode(response.data['access_token'], secret_key, algorithms=["HS256"])

        # 직접 생성한 토큰의 페이로드를 디코드
        expected_payload = jwt.decode(str(RefreshToken.for_user(test_user).access_token),
                                      secret_key,
                                      algorithms=["HS256"])

        assert response.status_code == 200

        # 중요한 정보(여기서는 user_id)가 일치하는지 확인
        assert returned_payload['user_id'] == expected_payload['user_id']

    def test_login_fail(self, test_user):
        client = APIClient()
        response = client.post(reverse('login'), {
            'email': test_user.email,
            'password': 'wrongpassword'
        })
        assert response.status_code == 401


@pytest.mark.django_db
class TestContactAPI:
    """ContactViewSet API에 대한 테스트"""

    def test_contact_create_authenticated(self, authenticated_api_client: APIClient):
        """인증된 상태에서 Contact 생성 API 검증"""
        data = {"name": "testcontactuser", "phone_number": "010-333-4444"}
        response = authenticated_api_client.post("/api/contacts/", data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Contact.objects.count() == 1
        assert Contact.objects.first().name == "testcontactuser"

        # TODO: 이메일, 전화번호, 웹사이트 유효성 검증

    def test_contact_list(self, authenticated_api_client: APIClient, test_contact_of_user: Contact):
        """인증된 상태에서 Contact 목록조회 API 검증"""
        response = authenticated_api_client.get("/api/contacts/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]["name"] == "testcontactuser"

        # TODO: 페이징이 잘되는지, 인증안된사람이 에러코드

    def test_contact_retrieve(self, authenticated_api_client: APIClient, test_contact_of_user: Contact):
        """인증된 상태에서 Contact 상세조회 API 검증"""
        response = authenticated_api_client.get(f"/api/contacts/{test_contact_of_user.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "testcontactuser"

    def test_contact_update(self, authenticated_api_client: APIClient, test_contact_of_user: Contact):
        """인증된 상태에서 Contact 전체수정 API 검증"""
        data = {"name": "updatedname", "phone_number": "010-555-6666"}
        response = authenticated_api_client.put(f"/api/contacts/{test_contact_of_user.id}/", data=data)
        test_contact_of_user.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert test_contact_of_user.name == "updatedname"

    def test_contact_partial_update(self, authenticated_api_client: APIClient, test_contact_of_user: Contact):
        """인증된 상태에서 Contact 부분수정 API 검증"""
        data = {"name": "partialupdatedname"}
        response = authenticated_api_client.patch(f"/api/contacts/{test_contact_of_user.id}/", data=data)
        test_contact_of_user.refresh_from_db()
        assert response.status_code == status.HTTP_200_OK
        assert test_contact_of_user.name == "partialupdatedname"

        # TODO: 이메일 처럼 특정 필드, 다른 사용자의 연락처 수정

    def test_contact_destroy(self, authenticated_api_client: APIClient, test_contact_of_user: Contact):
        """인증된 상태에서 Contact 삭제 API 검증"""
        response = authenticated_api_client.delete(f"/api/contacts/{test_contact_of_user.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Contact.objects.filter(id=test_contact_of_user.id).exists()

        # TODO: 연락처 리스트에 라벨 목록이 잘 나오는지 검증


@pytest.mark.django_db
class TestContactAPIOrdering:
    """ContactViewSet API의 정렬(ordering) 기능에 대한 테스트"""

    def setup_method(self):
        """
        `test_*` 테스트 메서드가 실행되기 전에 호출되는 메서드
        Constructor based DI(Dependency Injection)를 사용하여 테스트에 필요한 인스턴스를 생성/준비
        """
        user: User = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="testpass123"
        )

        client: APIClient = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        self.authenticated_api_client: APIClient = client
        self.contacts: List[Contact] = [
            Contact.objects.create(user=user, name="B Name", email="b@example.com", phone_number="1234567891"),
            Contact.objects.create(user=user, name="A Name", email="a@example.com", phone_number="1234567890"),
            Contact.objects.create(user=user, name="C Name", email="c@example.com", phone_number="1234567892")
        ]

    def test_order_by_name_ascending(self):
        """API를 통해 이름(name)을 기준으로 오름차순 정렬이 되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': 'name'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['name'] == "A Name"

    def test_order_by_name_descending(self):
        """API를 통해 이름(name)을 기준으로 내림차순 정렬이 되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': '-name'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['name'] == "C Name"

    def test_order_by_email_ascending(self):
        """API를 통해 이메일(email)을 기준으로 오름차순 정렬이 되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': 'email'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['email'] == "a@example.com"

    def test_order_by_email_descending(self):
        """API를 통해 이메일(email)을 기준으로 내림차순 정렬이 되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': '-email'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['email'] == "c@example.com"

    def test_order_by_phone_number_ascending(self):
        """API를 통해 전화번호(phone_number)을 기준으로 오름차순 정렬이 되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': 'phone_number'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['phone_number'] == "1234567890"

    def test_order_by_phone_number_descending(self):
        """API를 통해 전화번호(phone_number)을 기준으로 내림차순 정렬이 되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': '-phone_number'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['phone_number'] == "1234567892"

    def test_invalid_ordering_param(self):
        """API를 통해 유효하지 않은 정렬 파라미터를 제공했을 때 기본 정렬 방식(id)이 적용되는지 검증"""
        response = self.authenticated_api_client.get('/api/contacts/', {'ordering': 'invalid_field'})
        assert response.status_code == status.HTTP_200_OK
        # 기본 정렬은 id 기준이므로 첫 번째에 생성된 연락처가 나와야함
        assert response.data['results'][0]['id'] == self.contacts[0].id


@pytest.mark.django_db
class TestLabelAPI:
    """LabelViewSet API에 대한 테스트 케이스"""

    def test_label_list(self, authenticated_api_client: APIClient, test_label_of_user: Label):
        """API를 통해 Label 인스턴스 목록을 검증"""
        response = authenticated_api_client.get("/api/labels/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
        assert response.data['results'][0]["name"] == test_label_of_user.name

    def test_label_create(self, authenticated_api_client: APIClient):
        """API를 통해 Label 인스턴스 생성을 검증"""
        data = {"name": "testlabel"}
        response = authenticated_api_client.post("/api/labels/", data=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Label.objects.count() == 1
        assert Label.objects.first().name == "testlabel"

    def test_label_retrieve(self, authenticated_api_client: APIClient, test_label_of_user: Label):
        """API를 통해 특정 Label 인스턴스 상세 정보 조회를 검증"""
        response = authenticated_api_client.get(f"/api/labels/{test_label_of_user.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == test_label_of_user.name

    def test_label_update(self, authenticated_api_client: APIClient, test_label_of_user: Label):
        """API를 통해 Label 인스턴스 업데이트를 검증"""
        data = {"name": "updatedlabel"}
        response = authenticated_api_client.put(f"/api/labels/{test_label_of_user.id}/", data=data)
        assert response.status_code == status.HTTP_200_OK
        test_label_of_user.refresh_from_db()
        assert test_label_of_user.name == "updatedlabel"

    def test_label_destroy(self, authenticated_api_client: APIClient, test_label_of_user: Label):
        """API를 통해 Label 인스턴스 삭제를 검증"""
        response = authenticated_api_client.delete(f"/api/labels/{test_label_of_user.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Label.objects.count() == 0


@pytest.mark.django_db
class TestContactLabelAPI:
    """ContactLabelViewSet API에 대한 테스트"""

    def test_create_contact_label_without_duplication(self, authenticated_api_client: APIClient,
                                                      test_contact_of_user: Contact, test_label_of_user: Label):
        """API를 사용하여 중복되지 않는 [연락처-라벨]을 생성하는 기능 검증 (Best Case)"""
        data = {"contact": test_contact_of_user.id, "label": test_label_of_user.id}
        response = authenticated_api_client.post("/api/contact-labels/", data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_contact_label_with_duplication(self, authenticated_api_client: APIClient,
                                                   test_contact_label: ContactLabel):
        """API를 사용하여 이미 존재하는 [연락처-라벨]을 다시 생성하려 할 때의 응답을 테스트 (Worst Case)"""
        data = {"contact": test_contact_label.contact.id, "label": test_contact_label.label.id}
        response = authenticated_api_client.post("/api/contact-labels/", data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["detail"] == "This contact_label mapping already exists."

    def test_destroy_contact_label(self, authenticated_api_client: APIClient, test_contact_label: ContactLabel):
        """API를 사용하여 [연락처-라벨]을 삭제하는 기능 검증"""
        response = authenticated_api_client.delete(f"/api/contact-labels/{test_contact_label.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not ContactLabel.objects.filter(id=test_contact_label.id).exists()

    def test_destroy_contact_label_not_found(self, authenticated_api_client: APIClient):
        """API를 사용하여 존재하지 않는 [연락처-라벨]을 삭제 시도 검증"""
        response = authenticated_api_client.delete("/api/contact-labels/999999/")  # 999999는 존재하지 않는 ID로 가정
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data == {"detail": "Not found."}

    def test_create_contact_label_without_authentication(self, api_client: APIClient, test_contact_of_user: Contact,
                                                         test_label_of_user: Label):
        """비인증 상태에서 [연락처-라벨] 생성 시도 검증"""
        data = {"contact": test_contact_of_user.id, "label": test_label_of_user.id}
        response = api_client.post("/api/contact-labels/", data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_access_other_users_contact_label(self, authenticated_api_client: APIClient,
                                              test_contact_label: ContactLabel):
        """인증 상태에서 허용하지 않은 HTTP방식으로 [연락처-라벨]에 접근 시도 검증"""
        response = authenticated_api_client.get(f"/api/contact-labels/?contact={test_contact_label.contact.id}")
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
class TestLabelContactsAPI:
    """LabelContactsViewSet API에 대한 테스트"""

    @pytest.mark.django_db
    def test_contact_list_with_label(self, authenticated_api_client: APIClient, test_contact_of_user: ContactLabel,
                                     test_label_of_user: Label, test_contact_label: ContactLabel):
        """특정 라벨에 해당하는 연락처 목록을 반환하는 API 검증"""

        # API 호출을 통해 해당 라벨에 대한 연락처리스트 조회
        response = authenticated_api_client.get(f"/api/labels/{test_label_of_user.id}/contacts/")
        assert response.status_code == status.HTTP_200_OK
        assert any(contact['id'] == test_contact_label.contact.id for contact in response.data['results'])

        # contacts에 반환된 연락처들이 있는지 확인
        contacts = response.data['results']
        assert contacts is not None and len(contacts) > 0

        # test_contact_of_user의 ID가 contacts 목록에 있는지 확인
        assert any(contact['id'] == test_contact_of_user.id for contact in contacts)

    def test_contact_list_with_label_unauthenticated(self, client: APIClient, test_label_of_user: Label):
        """`비인증 회원`이 특정 라벨에 해당하는 연락처 목록을 반환하는 API 접근 시도 검증"""
        response = client.get(f"/api/labels/{test_label_of_user.id}/contacts/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_contact_list_without_label_id(self, authenticated_api_client: APIClient):
        """label_id가 없는경우 API 응답 검증"""
        response = authenticated_api_client.get("/api/labels//contacts/")
        assert response.status_code == status.HTTP_404_NOT_FOUND

        response = authenticated_api_client.get("/api/labels/contacts/")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_contact_list_with_empty_label(self, authenticated_api_client: APIClient, test_label_of_user: Label):
        """특정 라벨에 연락처가 매핑되지 않은 경우의 API 응답 검증"""
        response = authenticated_api_client.get(f"/api/labels/{test_label_of_user.id}/contacts/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 0
