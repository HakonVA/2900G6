from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='pages/recipes.html'), name='recipes-home'),
]   