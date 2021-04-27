from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    recipe_view
)

urlpatterns = [
    path('', view=recipe_view, name='recipe-home'),
]