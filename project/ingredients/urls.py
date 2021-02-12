from django.urls import include, path
from django.views.generic import TemplateView

# from .views import (

# )

urlpatterns = [
    path('', TemplateView.as_view(template_name='ingredients/ingredients-list.html'), name='ingred-list'),
]