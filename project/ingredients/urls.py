from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    get_ingredients
)

urlpatterns = [
    path('', get_ingredients, name='ingredients-list'),
]