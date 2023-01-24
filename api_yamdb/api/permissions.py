from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            return (user.is_authenticated
                    and user.is_admin or user.is_superuser)

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated:
            return (user.is_authenticated
                    and user.is_admin or user.is_superuser)


class IsAuthorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_moderator

    def has_object_permission(self, request, view, obj):
        return request.user.is_moderator


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
