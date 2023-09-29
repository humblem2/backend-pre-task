from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.v1.label import (
    serializers as ls,
)
from apps.addressbook import (
    models as m,
)


class LabelViewSet(viewsets.ModelViewSet):
    """Label 테이블에 대한 CRUD API"""

    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = m.Label.objects.all()
    serializer_class = ls.LabelSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """@overide 로그인 유저의 라벨"""
        if not self.request.user.is_authenticated:
            return m.Label.objects.none()  # 빈 쿼리셋 반환
        return m.Label.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ls.LabelUpdateSerializer
        return ls.LabelSerializer

    def perform_create(self, serializer):
        """@overide 라벨 생성시 로그인 유저 정보를 넣어줌"""
        serializer.save(user=self.request.user)
