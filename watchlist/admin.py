from django.contrib import admin

from watchlist.domain.models import Watchlist


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "movie", "created_at", "is_watched")
    list_filter = ("created_at", "is_watched")
    search_fields = ("user__username", "movie__title")
    ordering = ("-created_at",)
