from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User, Content
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, ContentSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrives user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class ContentViewSet(viewsets.ModelViewSet):
    """
    Creates new content
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)