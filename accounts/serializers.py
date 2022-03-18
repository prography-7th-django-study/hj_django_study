from http import HTTPStatus

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import serializers

from .jwt import generate_access_token
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
        password = data.get('password', None)
        user = User.objects.get(email=email)
        if user is None:
            return {
                'email':'None'
            }
        self.user = user
        return data


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