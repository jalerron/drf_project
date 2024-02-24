from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """проверка на владельца"""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsModerator(permissions.BasePermission):
    """проверка на модератора"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модератор').exists()
