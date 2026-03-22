from django.db import models

from subscription.models import Subscription


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=200)
    release_date = models.DateField()
    subscriptions = models.ManyToManyField(Subscription)
    poster_url = models.URLField()
    trailer_url = models.URLField()
    film_url = models.URLField()

    class Meta:
        ordering = ["id"]
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.title
