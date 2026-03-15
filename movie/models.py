from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=200)
    release_date = models.DateField()
    poster_url = models.URLField()
    trailer_url = models.URLField()
    film_url = models.URLField()

    def __str__(self):
        return self.title
