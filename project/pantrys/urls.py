from django.urls import include, path

from .views import (
    autocomplete,
    submitfood,
    pantry_index_view,
    user_ingredient_list_view,
    user_ingredient_create_view,
    user_ingredient_update_view,
    user_ingredient_delete_view,
)

app_name = "pantrys"
urlpatterns = [
    path('', view=pantry_index_view, name='index'),
    path('ingredients/', view=user_ingredient_list_view, name='ingredients'),
    path('ingredients/create/', view=user_ingredient_create_view, name='create'),
    path('ingredients/<int:pk>/update/', view=user_ingredient_update_view, name='update'),
    path('ingredients/<int:pk>/delete/', view=user_ingredient_delete_view, name='delete'),
    path('ingredients/create/autocomplete/', view=autocomplete, name='autocomplete'),
    path('ingredients/create/submitfood/', view=submitfood, name='submitfood'),
]   