from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet, basename="genre")

urlpatterns = [
    path("", include(router.urls)),
]
