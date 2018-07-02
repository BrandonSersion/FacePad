from rest_framework import serializers, mixins
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import User, Content, Rate, Comment, Friend


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes User destroy, list, retrieve.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',
            'last_name', 'date_of_birth', 'is_staff', 'friends',)
        read_only_fields = ('username',)


class EncryptUserSerializer(serializers.ModelSerializer):
    """
    Serializes User create, update.
    Encrypts password before it is stored.
    """
    def create(self, validated_data):
        """
        Overrides ModelSerializer create function.
        Encrypts the password field before saving it.
        """
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, validated_data):
        """
        Overrides ModelSerializer update function.
        Encrypts the password field before saving it.
        """
        user = User.objects.update_user(**validated_data)
        return user       

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
            'password', 'date_of_birth', 'friends',
        )
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

        
class ContentSerializer(serializers.ModelSerializer):
    """
    Serializes Content item create, destroy, list, retrieve, update.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    file_upload = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Content
        fields = ('id', 'file_upload', 'title', 'description', 'user', 'date_created',)


class RateSerializer(serializers.ModelSerializer):
    """
    Serializes Rate create, destroy, list, retrieve, update.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Rate
        fields = ('id', 'user', 'content', 'value', 'date_created',)

        validators = [
            UniqueTogetherValidator(
                queryset = Rate.objects.all(),
                fields = ('user', 'content',),
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes Comment create, destroy, list, retrieve, update.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'text', 'date_created',)


class FriendSerializer(serializers.ModelSerializer):
    """
    Serializes friend connection create, destroy, list, retrieve, update.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Friend
        fields = ('id', 'user', 'recipient',)

        validators = [
            UniqueTogetherValidator(
                queryset = Friend.objects.all(),
                fields = ('user', 'recipient',),
            )
        ]