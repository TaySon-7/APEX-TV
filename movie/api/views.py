from django.http import HttpResponse
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from movie.domain.exceptions import MovieNotFoundError, MovieSubscriptionMismatchError
from movie.domain.models import Genre
from movie.domain.models import Movie
from movie.api.serializers import MovieSerializer, GenreSerializer
from movie.services import movie_service


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class MoviePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 50


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    ordering = ['title']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = movie_service.create_movie(validated_data=serializer.validated_data)
        output_serializer = self.get_serializer(movie)
        headers = self.get_success_headers(output_serializer.data)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        movie_id = int(kwargs['pk'])
        try:
            movie_service.delete_movie(movie_id=movie_id)
        except MovieNotFoundError as exc:
            raise NotFound(str(exc)) from exc

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'], url_path='check-subscription-access')
    def check_subscription_access(self, request: Request, pk=None):
        raw_subscription_id = request.query_params.get("subscription_id")
        if raw_subscription_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            subscription_id = int(raw_subscription_id)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            movie_service.check_movie_allowed(movie_id=int(pk), subscription_id=subscription_id)
        except MovieNotFoundError as exc:
            raise NotFound(str(exc)) from exc
        except MovieSubscriptionMismatchError as exc:
            raise PermissionDenied(str(exc)) from exc

        return Response(status=status.HTTP_200_OK)


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
