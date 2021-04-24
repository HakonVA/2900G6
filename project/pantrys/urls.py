from django.urls import include, path

from .views import (
   user_ingredient_list_view,
   user_ingredient_create_view,
   user_ingredient_update_view,
   user_ingredient_delete_view,
)
app_name = "pantrys"
urlpatterns = [
    path('', view=user_ingredient_list_view, name='list'),
    path('create/', view=user_ingredient_create_view, name='create'),
    path('update/<int:pk>/', view=user_ingredient_update_view, name='update'),
    path('delete/<int:pk>/', view=user_ingredient_delete_view, name='delete'),
]   