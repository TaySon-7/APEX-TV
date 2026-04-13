from rest_framework import filters, permissions, viewsets

from watchlist.domain.models import Watchlist
from watchlist.api.serializers import WatchlistSerializer


class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "id"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Watchlist.objects.select_related("user", "movie").filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
