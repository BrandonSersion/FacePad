from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User, Content


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'auth_token', 'date_of_birth',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}
        validators = [
            UniqueTogetherValidator(
                queryset = User.objects.all(),
                fields = ('email', 'username')
            )
        ]

        
class ContentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields = ('id', 'title', 'date_created', 'description')