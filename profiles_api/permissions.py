from rest_framework import permissions


class UpdateProfile(permissions.BasePermission):
    """Allow user to update their profile only"""

    def has_object_permission(self, request, view, obj):
        """Check user can update their profile only"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.pk == obj.pk
