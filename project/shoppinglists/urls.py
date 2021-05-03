from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
    shopping_list_view,
    shopping_test_list_view,
    shopping_test_create_view,
    shopping_test_update_view,
    shopping_test_delete_view,
)

app_name = "shopping"
urlpatterns = [
    path('', view=shopping_list_view, name='list'),
    path('test/', view=shopping_test_list_view, name='list'),
    path('test/create', view=shopping_test_create_view, name='create'),
    path('test/<int:pk>/update/', view=shopping_test_update_view, name='update'),
    path('test/<int:pk>/delete/', view=shopping_test_delete_view, name='delete'),
]   