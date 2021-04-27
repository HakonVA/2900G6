from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    shoppinglist_view
)

urlpatterns = [
    path('', view=shoppinglist_view, name='shoppinglist-home'),
]