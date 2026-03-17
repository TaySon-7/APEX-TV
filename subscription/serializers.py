# subscriptions/serializers.py
from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            "id",
            "title",
            "monthly_price",
            "max_video_quality",
        )

    def validate_monthly_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Стоимость подписки должна быть больше 0.")
        return value
