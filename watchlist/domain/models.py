from django.conf import settings
from django.db import models


class Watchlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="watchlist_items",
    )
    movie = models.ForeignKey(
        "movie.Movie",
        on_delete=models.CASCADE,
        related_name="watchlist_items",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_watched = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_watchlist_per_user_movie",
            )
        ]
        verbose_name = "Watchlist"
        verbose_name_plural = "Watchlist"

    def __str__(self):
        return f"{self.user.username} -> {self.movie.title}"
