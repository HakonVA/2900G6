from django.contrib import admin

from .models import (
    Food,
    User_Food,
)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "fd_id",
        "fd_category",
        "scientific_name",
    ]


@admin.register(User_Food)
class User_FoodAdmin(admin.ModelAdmin):
    list_display = [
        "fd_id",
        "user",
    ]