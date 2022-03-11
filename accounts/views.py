from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()

    @action(methods=['get'], detail=False)
    def check_nickname(self, request):
        nickname = request.query_params.get('nickname')
        try:
            _nickname = User.objects.get(nickname=nickname)
            return Response(status=status.HTTP_409_CONFLICT)
        except:
            return Response(status=status.HTTP_200_OK)