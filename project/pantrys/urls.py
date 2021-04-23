from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
   user_ingredient_list_view,
   user_ingredient_create_view,
   user_ingredient_update_view,
)

urlpatterns = [
    path('pantrys/', view=user_ingredient_list_view, name='pantrys-list'),
    path('pantrys/create', view=user_ingredient_create_view, name='pantrys-create'),
    path('pantrys/<int:pk>', view=user_ingredient_update_view, name='pantrys-update'),
]   