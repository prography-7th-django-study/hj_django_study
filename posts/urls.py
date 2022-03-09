from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, PostCommentReadViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'post/(?P<postid>[0-9]+)/comment', PostCommentReadViewSet, basename='comment-read')
urlpatterns = router.urls