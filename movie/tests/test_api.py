import datetime

from django.db.models import Model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from movie.domain.models import Genre, Movie
from subscription.domain.models import Subscription


class MovieApiTests(APITestCase):
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

        self.movie = Movie.objects.create(
            title="title",
            description="description",
            duration=100,
            genre=self.genre,
            release_date=datetime.datetime.now(),
            poster_url="https://example.com",
            trailer_url="https://example.com",
            film_url="https://example.com",
        )
        self.movie.subscriptions.add(self.subscription)

    def test_create_movie(self):
        url = reverse("movie-list")
        data = {
            "title": "title",
            "description": "description",
            "duration": 100,
            "genre": self.genre.id,
            "release_date": datetime.date.today(),
            "subscriptions": [self.subscription.id],
            "poster_url": "https://example.com/",
            "trailer_url": "https://example.com/",
            "film_url": "https://example.com/",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created = Movie.objects.get(id=response.data["id"])
        self.assertEqual(created.subscriptions.count(), 1)

    def test_delete_movie_success(self):
        url = reverse("movie-detail", args=[self.movie.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())

    def test_delete_movie_failure(self):
        url = reverse("movie-detail", args=[99])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_check_subscription_access_success(self):
        url = reverse("movie-check-subscription-access", args=[self.movie.id])
        response = self.client.get(f"{url}?subscription_id={self.subscription.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_subscription_access_failure(self):
        url = reverse("movie-check-subscription-access", args=[self.movie.id])
        response = self.client.get(f"{url}?subscription_id={self.premium.id}")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_check_subscription_access_bad_request(self):
        url = reverse("movie-check-subscription-access", args=[self.movie.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        url = reverse("movie-check-subscription-access", args=[99])
        response = self.client.get(f"{url}?subscription_id={self.subscription.id}")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
