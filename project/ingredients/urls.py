from django.urls import include, path

from .views import (
    pantry_index_view,
    pantry_delete_all_view,
)

urlpatterns = [
    path('', view=pantry_index_view, name='pantry-home'),
    path('delete-all', view=pantry_delete_all_view, name='delete-all'),
]