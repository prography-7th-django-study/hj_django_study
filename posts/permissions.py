from django.contrib.auth import get_user_model
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    pass