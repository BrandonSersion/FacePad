from rest_framework import permissions
from .models import Friend


class IsUser(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsUserOrFriend(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            is_on_friend_list = Friend.objects.filter(user=obj.user, recipient=request.user)
            return is_on_friend_list
        else:
            return obj.user == request.user or request.user.is_staff
