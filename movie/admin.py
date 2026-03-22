from django.contrib import admin

from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'genre', 'duration', 'release_date')
    list_filter = ('genre', 'release_date', 'subscriptions')
    search_fields = ('title', 'description', 'genre')
    list_per_page = 20
