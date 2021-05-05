from django.contrib import admin

from .models import(
    Shopping,
)

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