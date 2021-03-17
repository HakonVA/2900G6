from django.urls import include, path

from .views import (
    pantry_index_view,
    pantry_DeleteAll_view,
    # pantry_list_view,
    # pantry_create_view,
)

urlpatterns = [
    path('', view=pantry_index_view, name='pantry-home'),
    path('deleteAll', view=pantry_DeleteAll_view, name='Delete-all'),
]