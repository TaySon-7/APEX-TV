from django.db import models


# Create your models here.
class Subscription(models.Model):
    QUALITY_CHOICES = [
        ("480p", "480p"),
        ("720p", "720p"),
        ("1080p", "1080p"),
        ("4k", "4k"),
    ]

    title = models.CharField(max_length=50, unique=True)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)
    max_video_quality = models.CharField(max_length=10, choices=QUALITY_CHOICES)

    class Meta:
        ordering = ["id"]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return self.title
