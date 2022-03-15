from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from posts.models import Post, Comment, Member
from posts.serializers import PostSerializer, MemberSerializer, PostSummarizeSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PostSummarizeSerializer
        else:
            return PostSerializer



class CommentViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,GenericViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostCommentReadViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post__id=post_id)


class MemberViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,GenericViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()