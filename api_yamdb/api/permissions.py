from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return (user.is_authenticated
                and (user.is_admin or user.is_superuser))


class IsModerator(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_moderator


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAuthenticatedAndPOSTrequest(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method == 'POST' and request.user.is_authenticated


class GenrePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or (user.is_authenticated
                    and (user.is_admin or user.is_superuser)))
