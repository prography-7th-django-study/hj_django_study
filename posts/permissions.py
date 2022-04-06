from rest_framework import permissions


class IsAuthorOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        return

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            if request.method in ('GET', 'HEAD', 'OPTIONS', 'POST',):
                return True
            else:
                return obj.author == request.user
        else:
            return False