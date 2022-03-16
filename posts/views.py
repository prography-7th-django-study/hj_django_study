from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from posts.models import Post, Comment, Member
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, MemberSerializer, PostSummarizeSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


    def get_serializer_class(self):
        if self.action == "list":
            return PostSummarizeSerializer
        else:
            return PostSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk):
        comments = Comment.objects.filter(post__id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def members(self, request, pk):
        members = Member.objects.filter(post__id=pk)
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class CommentViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,GenericViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MemberViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
