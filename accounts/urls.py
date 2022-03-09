from rest_framework.routers import DefaultRouter

from accounts.views import ProfileViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
urlpatterns = router.urls