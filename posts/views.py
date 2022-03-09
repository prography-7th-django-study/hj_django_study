from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from posts.models import Post, Comment
from posts.serializers import PostSerializer, PostListSerializer, CommentWriteSerializer, \
    CommentReadSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        else:
            return PostSerializer


class CommentViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,GenericViewSet):

    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CommentReadSerializer
        else:
            return CommentWriteSerializer

class PostCommentReadViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentReadSerializer

    def get_queryset(self):
        post_id = self.kwargs['postid']
        return Comment.objects.filter(post__id=post_id)