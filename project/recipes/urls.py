from django.urls import include, path

from .views import (
    recipe_list_view,
    recipe_detail_view,
)

app_name = "recipes"
urlpatterns = [
    path('', view=recipe_list_view, name='list'),
    path('<int:pk>/', view=recipe_detail_view, name='detail'),
]   