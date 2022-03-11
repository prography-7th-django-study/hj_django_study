from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, PostCommentReadViewSet, MemberViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'posts/(?P<postid>[0-9]+)/comments', PostCommentReadViewSet, basename='comment-read')
router.register(r'members', MemberViewSet, basename='member')
urlpatterns = router.urls