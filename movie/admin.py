from django.contrib import admin
from movie.models import Genre
from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'genre', 'duration', 'release_date')
    list_filter = ('genre__title', 'release_date', 'subscriptions')
    search_fields = ('title', 'description', 'genre__title')
    list_per_page = 20

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    search_fields = ('title',)
    list_per_page = 10
