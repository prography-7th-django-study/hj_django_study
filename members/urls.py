from rest_framework.routers import DefaultRouter

from .views import MemberViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'member', MemberViewSet, basename='member')
urlpatterns = router.urls