from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User, Content, Rate, Comment
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, ContentSerializer, RateSerializer, CommentSerializer


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
    Creates, updates, deletes, lists, retrieves contents
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (IsUserOrReadOnly,)


class RateViewSet(viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, retrieves rates
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = (IsUserOrReadOnly,)



class CommentViewSet(viewsets.ModelViewSet):
    """
    Creates, updates, deletes, lists, retrieves comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsUserOrReadOnly,)