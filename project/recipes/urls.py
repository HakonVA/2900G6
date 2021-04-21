from django.urls import include, path

from .views import (
    recipe_list_view,
    recipe_detail_view,
)

urlpatterns = [
    path('recipes/', view=recipe_list_view, name='recipes-list'),
    path('recipes/<int:pk>', view=recipe_detail_view, name='recipes-detail'),
]   