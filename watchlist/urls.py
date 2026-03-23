from django.urls import include, path
from rest_framework.routers import DefaultRouter

from watchlist.views import WatchlistViewSet

router = DefaultRouter()
router.register("watchlist", WatchlistViewSet, basename="watchlist")

urlpatterns = [
    path("", include(router.urls)),
]
