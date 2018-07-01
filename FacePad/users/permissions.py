from rest_framework import permissions
from .models import Friend


class IsUser(permissions.BasePermission):
    """
    Object-level permission
    Read permission: User, Admin
    Write permission: User, Admin
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsUserOrFriend(permissions.BasePermission):
    """
    Object-level permission
    Read permission: User, Friend, Admin
    Write permission: User, Admin
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            request_user_is_friend_of_obj_user = \
                Friend.objects.filter(user=obj.user, recipient=request.user)
            return request_user_is_friend_of_obj_user or request.user.is_staff
        else:
            return obj.user == request.user or request.user.is_staff
