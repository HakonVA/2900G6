from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    ingredient_index_view,
    ingredient_deleteAll_view,
    autocomplete
)

urlpatterns = [
    path('', view=ingredient_index_view, name='ingredients-home'),
    # path('', view=ingredient_index_view, name='ingredients-home'),
    path('deleteAll', ingredient_deleteAll_view, name='deleteAll'),
    path("autocomplete", autocomplete, name="autocomplete")
]