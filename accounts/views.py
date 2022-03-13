from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import ProfileSerializer, UserSerailizer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.signup or self.login:
            return ProfileSerializer
        else:
            return UserSerailizer

    @action(methods=['get'], detail=False)
    def check_nickname(self, request):
        nickname = request.query_params.get('nickname')
        try:
            _nickname = User.objects.get(nickname=nickname)
            return Response(status=status.HTTP_409_CONFLICT)
        except:
            return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def signup(self, request):
        serializer = UserSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def login(self, request):
        return Response(status=status.HTTP_201_CREATED)