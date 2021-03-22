import rest_framework
from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, req, view, obj):
        if req.method in permissions.SAFE_METHODS:
            return True

        if obj.owner is None:
            return True

        return obj.owner == request.user