from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AirplaneViewSet, BookViewSet, CarViewSet, MovieViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("car", CarViewSet)
router.register("movie", MovieViewSet)
router.register("book", BookViewSet)
router.register("airplane", AirplaneViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
