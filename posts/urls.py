from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, MemberViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
member_router = DefaultRouter(trailing_slash=False)
member_router.register(r'members', MemberViewSet, basename='member')
urlpatterns = [
    path("", include(router.urls)),
    path("", include(member_router.urls)),
]