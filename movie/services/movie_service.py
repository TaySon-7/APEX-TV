from typing import Any

from django.db import transaction

from movie.domain.exceptions import MovieNotFoundError, MovieSubscriptionMismatchError
from movie.domain.models import Movie


def get_movie(movie_id: int) -> Movie:
    try:
        return Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist as exc:
        raise MovieNotFoundError(movie_id) from exc


@transaction.atomic
def create_movie(*, validated_data: dict[str, Any]) -> Movie:
    subscriptions = validated_data.pop("subscriptions", [])
    movie = Movie.objects.create(**validated_data)
    if subscriptions:
        movie.subscriptions.set(subscriptions)
    return movie


@transaction.atomic
def delete_movie(movie_id: int) -> None:
    movie = get_movie(movie_id)
    movie.delete()


def check_movie_allowed(*, movie_id: int, subscription_id: int) -> Movie:
    movie = get_movie(movie_id)
    if not movie.subscriptions.filter(pk=subscription_id).exists():
        raise MovieSubscriptionMismatchError(movie_id, subscription_id)
    return movie
