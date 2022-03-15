from django.urls import include, path
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet, LoginView, SignupView


router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    #path('', include(router.urls)),
    path('users/signup',SignupView.as_view()),
    path('users/login', LoginView.as_view()),
]