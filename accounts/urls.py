from rest_framework.routers import DefaultRouter

from accounts.views import ProfileViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'users', ProfileViewSet, basename='profile')
urlpatterns = router.urls