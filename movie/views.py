from django.http import HttpResponse
from rest_framework import viewsets

from movie.models import Movie
from movie.serializers import MovieSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
