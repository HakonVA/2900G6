from django.contrib import admin

from .models import(
    UserIngredient,
)

@admin.register(UserIngredient)
class UserIngredientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'food',
        'user',
    ]