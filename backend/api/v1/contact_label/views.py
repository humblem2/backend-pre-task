from typing import Union

from django.http import QueryDict
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.v1 import (
    paginators as pn,
    permissions as pm,
)
from api.v1.contact_label import (
    serializers as cls,
)
from apps.addressbook import (
    models as m,
)


class ContactLabelViewSet(viewsets.ModelViewSet):
    """ContactLabel 테이블에 대한 CRUD API"""

    http_method_names = ['post', 'delete', 'head', 'options']
    queryset = m.ContactLabel.objects.all()
    pagination_class = pn.DefaultContactLabelPagination
    serializer_class = cls.ContactLabelSerializer
    permission_classes = [IsAuthenticated, pm.IsOwnerOfContactLabel]
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        """로그인 유저의 연락처-라벨 매핑을 반환"""
        if not self.request.user.is_authenticated:
            return m.ContactLabel.objects.none()

        queryset = m.ContactLabel.objects.filter(contact__user=self.request.user)

        contact_id = self.request.query_params.get('contact', None)
        if contact_id is not None:
            queryset = queryset.filter(contact=contact_id)

        label_id = self.request.query_params.get('label', None)
        if label_id is not None:
            queryset = queryset.filter(label=label_id)

        return queryset

    def create(self, request, *args, **kwargs):
        """ContactLabel 테이블의 매핑을 생성하며, DB의 `(contact, label) 조합` 중복 검사"""

        if self._is_duplicate_data(request.data):
            return Response({"detail": "This contact_label mapping already exists."},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def _is_duplicate_data(self, data: Union[QueryDict, dict]) -> bool:
        """연락처-라벨 매핑을 생성할 때, (contact, label) 조합이 이미 존재하는지 여부"""

        contact_id = data.get('contact')
        label_id = data.get('label')
        return m.ContactLabel.objects.filter(contact_id=contact_id, label_id=label_id).exists()
