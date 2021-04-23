from django.contrib import admin

from .models import (
    Food,
    Ingredient,
    Recipe,
)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'food',
        'amount',
        'unit',
    ]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'data_created',
    ]
