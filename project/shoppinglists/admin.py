from django.contrib import admin

from .models import(
    ShoppingEntry,
    ShoppingList,
    Shopping,
)

@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
    ]

@admin.register(ShoppingEntry)
class ShoppingEntryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'recipes',
        'food', 
        'unit',
        'amount',
        'checked',
    ]

@admin.register(Shopping)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'name',
        'unit',
        'amount',
        'checked',
    ]