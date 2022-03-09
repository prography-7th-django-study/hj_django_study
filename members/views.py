from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from members.models import Member
from members.serializers import MemberSerializer


class MemberViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,GenericViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()