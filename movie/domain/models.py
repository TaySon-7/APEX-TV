from django.db import models

from subscription.domain.models import Subscription

class Genre(models.Model):
    """
    модель жанра фильма
    """
    title = models.CharField(max_length=100, verbose_name='Название жанра', unique=True)
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        ordering = ['title']
        verbose_name = "жанр"
        verbose_name_plural = "жанры"

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
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