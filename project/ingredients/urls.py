from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    ingredient_index_view,
    ingredient_deleteAll_view,
)

urlpatterns = [
    path('', ingredient_index_view, name='ingredients-home'),
    path('deleteAll', ingredient_deleteAll_view, name='deleteAll'),
]