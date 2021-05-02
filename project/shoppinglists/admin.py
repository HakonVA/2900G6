from django.contrib import admin

from .models import(
    ShoppingEntry,
    ShoppingList,
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
        'food',
        'unit',
        'amount',
        'checked',
    ]