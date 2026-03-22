from django.contrib import admin

# Register your models here.
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "monthly_price", "max_video_quality",)
    search_fields = ("title",)
    list_filter = ("max_video_quality",)

