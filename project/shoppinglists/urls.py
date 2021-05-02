from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    shopping_list_view,
)

app_name = "shopping"
urlpatterns = [
    path('', view=shopping_list_view, name='list'),
]   