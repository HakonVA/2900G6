from django.contrib import admin

from .models import (
    Food,
    Pantry,
)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "fd_id",
        "scientific_name",
        "category",
    ]


@admin.register(Pantry)
class PantryAdmin(admin.ModelAdmin):
    list_display = [
        "py_id",
        "name",
        "user",
    ]