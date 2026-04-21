import datetime

from django.test import TestCase

from movie.domain.exceptions import MovieSubscriptionMismatchError
from movie.domain.models import Genre, Movie
from movie.services import movie_service
from subscription.domain.models import Subscription


class MovieServiceTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            title="title",
            description="description",
            slug="slug",
        )
        self.subscription = Subscription.objects.create(
            title="title",
            monthly_price="100",
            max_video_quality="720p",
        )

        self.premium = Subscription.objects.create(
            title="title1",
            monthly_price="1000",
            max_video_quality="720p",
        )

    def _movie_data(self):
        return {
            "title": "title",
            "description": "description",
            "duration": 100,
            "genre": self.genre,
            "subscriptions": [self.subscription],
            "release_date": datetime.date.today(),
            "poster_url": "https://example.com/",
            "trailer_url": "https://example.com/",
            "film_url": "https://example.com/",
        }

    def test_create_movie(self):
        data = self._movie_data()
        movie = movie_service.create_movie(validated_data=data)

        self.assertEqual(movie.title, "title")
        self.assertEqual(movie.subscriptions.count(), 1)

    def test_delete_movie_success(self):
        data = self._movie_data()
        movie = movie_service.create_movie(validated_data=data)

        movie_service.delete_movie(movie_id=movie.id)

        self.assertFalse(Movie.objects.filter(id=movie.id).exists())

    def test_delete_movie_not_found(self):
        with self.assertRaises(movie_service.MovieNotFoundError):
            movie_service.delete_movie(movie_id=999)

    def test_ensure_movie_allowed_success(self):
        data = self._movie_data()
        movie = movie_service.create_movie(validated_data=data)

        result = movie_service.check_movie_allowed(movie_id=movie.id, subscription_id=self.subscription.id)

        self.assertEqual(result.id, movie.id)

    def test_ensure_movie_allowed_subscription_mismatch(self):
        data = self._movie_data()
        movie = movie_service.create_movie(validated_data=data)

        with self.assertRaises(MovieSubscriptionMismatchError):
            movie_service.check_movie_allowed(
                movie_id=movie.id,
                subscription_id=self.premium.id,
            )
