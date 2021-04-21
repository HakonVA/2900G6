from django.urls import include, path
from django.views.generic import TemplateView

from .views import (
   user_ingredient_list_view,
)

urlpatterns = [
    path('pantrys/', view=user_ingredient_list_view, name='pantrys-list'),
]   

# http://127.0.0.1:8000/pantrys/
# http://127.0.0.1:8000/pantrys/add
# http://127.0.0.1:8000/pantrys/<int:pk>
# http://127.0.0.1:8000/pantrys/<int:pk>/update
# http://127.0.0.1:8000/pantrys/<int:pk>/delete