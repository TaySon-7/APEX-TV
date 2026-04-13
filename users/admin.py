from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.domain.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "id",
        "username",
        "full_name",
        "email",
        "phone",
        "current_subscription",
        "watchlist",
        "is_staff",
    )
    search_fields = ("username", "full_name", "email", "phone")
    fieldsets = DjangoUserAdmin.fieldsets + (
        (
            "Дополнительно",
            {
                "fields": (
                    "full_name",
                    "current_subscription",
                    "watchlist",
                    "phone",
                )
            },
        ),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        (
            "Дополнительно",
            {
                "fields": (
                    "full_name",
                    "email",
                    "phone",
                    "current_subscription",
                )
            },
        ),
    )
