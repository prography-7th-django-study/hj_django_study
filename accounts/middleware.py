from rest_framework import status
from rest_framework.permissions import SAFE_METHODS

from .models import User
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from .jwt import decode_jwt
from jwt.exceptions import ExpiredSignatureError
from http import HTTPStatus


class JsonWebTokenMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if (
                request.path != "/api/users/signup"
                and request.path != "/api/users/login"
                and "admin" not in request.path
                and request.method not in SAFE_METHODS
            ):
                print(request.path)
                # Except signup and login
                headers = request.headers
                # Get Authorization header or None
                access_token = headers.get("Authorization", None)
                print(access_token)
                # If access_token isn't exist
                if not access_token:
                    raise PermissionDenied()

                # Decode JWT token
                print('?')
                payload = decode_jwt(access_token)
                print('??')
                # Get user from decoded jwt payload
                email = payload.get("aud", None)

                # If username is None
                if not email:
                    raise PermissionDenied()

                # Get user object using username
                User.objects.get(email=email)
            response = self.get_response(request)

            return response

        except (PermissionDenied, User.DoesNotExist):
            return JsonResponse(
                {"error": "Authorization Error"}, status=HTTPStatus.UNAUTHORIZED
            )

        except ExpiredSignatureError:
            return JsonResponse(
                {"error": "Expired token. Please log in again."},
                status=status.FORBIDDEN,
            )