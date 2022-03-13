from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, PostCommentReadViewSet, MemberViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
comment_router = DefaultRouter(trailing_slash=False)
comment_router.register(r'comments', PostCommentReadViewSet, basename='comment-read')
member_router = DefaultRouter(trailing_slash=False)
member_router.register(r'members', MemberViewSet, basename='member')
urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:post_pk>/", include(comment_router.urls)),
    path("posts/<int:post_pk>/", include(member_router.urls)),
]
