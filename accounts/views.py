from http import HTTPStatus
from json import loads
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import IntegrityError
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.jwt import generate_access_token
from accounts.models import User
from accounts.serializers import UserSerializer, UserSignupSerializer, UserLoginSerializer


@api_view(["GET"])
def ping(request):
    res = {
        "server": "on"
    }
    return Response(res, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'login':
            return UserLoginSerializer
        elif self.action == 'signup':
            return UserSignupSerializer
        else:
            return UserSerializer


    @action(methods=['get'], detail=False)
    def check_nickname(self, request):
        nickname = request.query_params.get('nickname')
        try:
            _nickname = User.objects.get(nickname=nickname)
            return Response(status=status.HTTP_409_CONFLICT)
        except:
            return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def login(self, request):
        data = {}
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'message':'Request Body Error.'},status=status.HTTP_409_CONFLICT)
        user = serializer.user
        data['access_token'] = generate_access_token(user.email)
        data['email'] = user.email
        data['id'] = user.id
        data['nickname'] = user.nickname
        return Response(data, status=status.HTTP_200_OK)


    @action(methods=['post'], detail=False)
    def signup(self, request):
        data = {}
        serializer = UserSignupSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'message':'Request Body Error.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            user = serializer.user
            data['access_token'] = generate_access_token(user.email)
            data['email'] = user.email
            data['id'] = user.id
            data['nickname'] = user.nickname
            return Response(data,status=status.HTTP_201_CREATED)
        return Response({'message':'duplicate email'},status=status.HTTP_409_CONFLICT)