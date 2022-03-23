from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'nickname',
            'description',
            'image',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, data):
        email = data.get('email',None)
        print(email)
        password = data.get('password', None)
        print(password)
        user = User.objects.get(email=email)
        if user is None:
            return None
        return user

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'nickname',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        email = validated_data['email']
        nickname = validated_data['nickname']
        password = validated_data['password']
        user = User.objects.create(
            email = email,
            nickname = nickname,
        )
        user.set_password(password)
        user.save()
        self.user = user
        return user

