from http import HTTPStatus
from json import loads
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import IntegrityError
from django.http import HttpResponseNotAllowed, JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.jwt import generate_access_token
from accounts.models import User
from accounts.serializers import UserSerializer, AuthenticateSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering_fields = ['id']

    @action(methods=['get'], detail=False)
    def check_nickname(self, request):
        nickname = request.query_params.get('nickname')
        try:
            _nickname = User.objects.get(nickname=nickname)
            return Response(status=status.HTTP_409_CONFLICT)
        except:
            return Response(status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        data = {}
        try:
            json_body = loads(request.body)
            email = json_body.get("email", None)
            password = json_body.get("password", None)

            if not email or not password:
                raise ValueError()

            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise ValueError()

            data["access_token"] = generate_access_token(email)
            data["email"] = email
            data["nickname"] = user.nickname
            status = HTTPStatus.OK

        except (ValueError, User.DoesNotExist):
            # Login request validation exception
            data["error"] = "Invalid form. Please fill it out again."
            status = HTTPStatus.BAD_REQUEST

        return JsonResponse(data, status=status)



class SignupView(APIView):

    def post(self, request):
        data = {}
        status = HTTPStatus.CREATED
        try:
            json_body = loads(request.body)
            email = json_body.get("email", None)
            password = json_body.get("password", None)
            nickname = json_body.get("nickname", None)

            if not email or not password:
                raise ValueError()

            email_validator = ASCIIUsernameValidator(
                message="Please check the email condition."
            )

            email_validator(email)
            validate_password(password)

            user = User.objects.create(email=email,nickname=nickname)
            user.set_password(password)
            user.save()

            data["access_token"] = generate_access_token(email)
            data["email"] = email
            data['id'] = user.id
            data['nickname'] = user.nickname

        except ValidationError as e:
            data["error"] = e.messages
            status = HTTPStatus.BAD_REQUEST

        except IntegrityError:
            data["error"] = "Duplicate user name. Please use a different name."
            status = HTTPStatus.BAD_REQUEST

        except ValueError:
            data["error"] = "Invalid form. Please fill it out again."
            status = HTTPStatus.BAD_REQUEST

        return JsonResponse(data, status=status)