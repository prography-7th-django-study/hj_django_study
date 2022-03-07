from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
urlpatterns = router.urls