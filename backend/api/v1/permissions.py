from rest_framework.permissions import BasePermission


class IsOwnerOfContactLabel(BasePermission):
    """연락처 라벨의 소유자만 해당 라벨을 수정하거나 삭제할 수 있는 권한"""

    def has_object_permission(self, request, view, obj):
        # Check if the current user is the owner of the contact label.
        return obj.contact.user == request.user


class IsOwnerOfContact(BasePermission):
    """연락처의 소유자만 CRUD 작업을 수행 권한"""

    def has_object_permission(self, request, view, obj):
        # Check if the current user is the owner of the contact.
        return obj.user == request.user
