from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from accounts.models import User
from accounts.serializers import ProfileSerializer

@api_view(['GET'])
def duplicate_check(request):
    nickname = request.GET.get('nickname')
    try:
        _nickname = User.objects.get(nickname=nickname)
    except:
        _nickname = None
    if _nickname is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {
        'duplicate': duplicate
    }
    return JsonResponse(context)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()