from django.urls import include, path
from django.views.generic import TemplateView

# from .views import (
   
# )

urlpatterns = [
    path('pantrys/', TemplateView.as_view(template_name='pantrys/pantrys_detail.html'), name='pantrys-detail'),
]   