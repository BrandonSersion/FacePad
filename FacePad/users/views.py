from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import User, Content, Rate, Comment
from .permissions import IsUser, IsUserOrFriend
from .serializers import CreateUserSerializer, UserSerializer, ContentSerializer, RateSerializer, CommentSerializer
from .mixins import MixedPermissionModelMixin


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrives user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUser,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class ContentViewSet(MixedPermissionModelMixin,
                     viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, retrieves contents
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes_by_action = {
        'create': [IsUser],
        'update': [IsAdminUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],
    }


class RateViewSet(MixedPermissionModelMixin,
                  viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, retrieves rates
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes_by_action = {
        'create': [IsUserOrFriend],
        'update': [IsAdminUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],
    }


class CommentViewSet(MixedPermissionModelMixin,
                     viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, retrieves comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_by_action = {
        'create': [IsUserOrFriend],
        'update': [IsAdminUser],
        'delete': [IsAdminUser],
        'list': [IsAdminUser],
        'retrieve': [IsUserOrFriend],
    }