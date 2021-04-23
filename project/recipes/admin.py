from django.contrib import admin

# Register your models here.

from .models import Recipe, RecipeFood

admin.site.register(Recipe)
admin.site.register(RecipeFood)