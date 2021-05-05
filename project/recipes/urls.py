from django.urls import include, path

from .views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_to_shopping_list,
)

app_name = "recipes"
urlpatterns = [
    path('', view=recipe_list_view, name='list'),
    path('<int:pk>/', view=recipe_detail_view, name='detail'),
    path('<int:pk>/add_to_shopping/', view=recipe_to_shopping_list, name='shopping'),
] 