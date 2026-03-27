from django.http import HttpResponse
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from movie.models import Genre
from movie.models import Movie
from movie.serializers import MovieSerializer, GenreSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MoviePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 50

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']

class GenrePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 50

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = GenrePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'slug']
    ordering_fields = ['title']
    ordering = ['title']