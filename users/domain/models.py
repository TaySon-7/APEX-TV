from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    current_subscription = models.ForeignKey(
        "subscription.Subscription",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    watchlist = models.ForeignKey(
        "watchlist.Watchlist",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="selected_by_users",
    )
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='cinemausers_user_set',  # Уникальное имя
        related_query_name='cinemauser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='cinemausers_user_set',  # Уникальное имя
        related_query_name='cinemauser',
    )


    def clean(self):
        super().clean()

        if self.watchlist.user_id is None or self.pk is None:
            return

        if self.watchlist.user_id != self.pk:
            raise ValidationError(
                {"watchlist": "Выбранный watchlist должен принадлежать этому пользователю."}
            )

    def __str__(self):
        return self.full_name or self.username
