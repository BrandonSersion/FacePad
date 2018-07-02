from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import User, Content, Rate, Comment, Friend


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',
            'last_name', 'date_of_birth', 'is_staff', 'friends',)  # TODO is_staff shouldnt be editable
        read_only_fields = ('username',)


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'username',
            'password', 'date_of_birth', 'friends',
        )
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

        
class ContentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    file_upload = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Content
        fields = ('id', 'file_upload', 'title', 'description', 'user', 'date_created',)


class RateSerializer(serializers.ModelSerializer):
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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'text', 'date_created',)


class FriendSerializer(serializers.ModelSerializer):
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