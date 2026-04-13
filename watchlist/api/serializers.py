from rest_framework import serializers

from watchlist.domain.models import Watchlist


class WatchlistSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Watchlist
        fields = ("id", "user", "movie", "movie_title", "created_at", "is_watched")
        read_only_fields = ("user", "created_at")

    def validate(self, attrs):
        request = self.context.get("request")
        movie = attrs["movie"]

        if request is None:
            return attrs

        existing_items = Watchlist.objects.filter(user=request.user, movie=movie)
        if self.instance is not None:
            existing_items = existing_items.exclude(pk=self.instance.pk)

        if existing_items.exists():
            raise serializers.ValidationError(
                {"movie": "Этот фильм уже находится в watchlist пользователя."}
            )

        return attrs
