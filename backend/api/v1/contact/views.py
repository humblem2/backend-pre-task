from rest_framework import viewsets, mixins, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.v1 import (
    paginators as pn,
    permissions as pm,
)
from api.v1.contact import (
    serializers as cs,
)
from apps.addressbook import (
    models as m,
)


class ContactViewSet(viewsets.ModelViewSet):
    """Contact 테이블에 대한 CRUD API"""

    queryset = m.Contact.objects.all()
    pagination_class = pn.DefaultContactPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """@overide 로그인 유저의 연락처 및 정렬"""
        if not self.request.user.is_authenticated:
            return m.Contact.objects.none()

        queryset = m.Contact.objects.all()
        ordering = self.request.query_params.get('ordering', None)

        if ordering in ['name', 'email', 'phone_number', '-name', '-email', '-phone_number', '-id']:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('id')

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """현재 요청 액션에 따라 적절한 시리얼라이저를 반환"""
        if self.action == 'list':
            return cs.ContactListSerializer
        else:
            return cs.ContactDetailSerializer

    def perform_create(self, serializer):
        """@overide 연락처 생성 시 필수 필드인 로그인 유저 정보를 넣어 DB에 저장 (labels 필드는 동시에 저장하지 않음)"""
        serializer.save(user=self.request.user)


class LabelContactsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """`특정 라벨`에 대응되는 `연락처 리스트`"""

    queryset = m.Contact.objects.all()
    serializer_class = cs.ContactListSerializer
    pagination_class = pn.DefaultContactPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, pm.IsOwnerOfContact]

    def get_queryset(self):
        """@overide URL에서 `label` 쿼리 파라미터를 기반으로 특정 라벨에 해당하는 연락처리스트를 반환"""
        if not self.request.user.is_authenticated:
            return m.Contact.objects.none()

        queryset = m.Contact.objects.filter(user=self.request.user)

        label_id = self.kwargs.get('label_id', None)
        if not label_id:
            raise exceptions.ValidationError("label_id is required in the path.")

        contact_ids = m.ContactLabel.objects.filter(label=label_id).values_list('contact', flat=True)
        queryset = queryset.filter(id__in=contact_ids)

        return queryset

