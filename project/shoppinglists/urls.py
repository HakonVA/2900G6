from django.urls import path

from .views import (
    shopping_list_view,
    shopping_create_view,
    shopping_update_view,
    shopping_delete_view,
    shopping_checkout,

)

app_name = "shopping"
urlpatterns = [
    path('', view=shopping_list_view, name='list'),
    path('create', view=shopping_create_view, name='create'),
    path('<int:pk>/update/', view=shopping_update_view, name='update'),
    path('<int:pk>/delete/', view=shopping_delete_view, name='delete'),
    path('checkout/', view=shopping_checkout, name='checkout'),
]   