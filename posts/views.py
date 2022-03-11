from rest_framework import viewsets, status, mixins
from rest_framework.viewsets import GenericViewSet

from posts.models import Post, Comment, Member
from posts.serializers import PostSerializer, CommentWriteSerializer, \
    CommentReadSerializer, MemberSerializer, PostSummerizeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PostSummerizeSerializer
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


class MemberViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,GenericViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()