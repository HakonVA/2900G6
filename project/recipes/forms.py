from django.forms import ModelForm
from .models import Recipe

class RecipeCreateForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name"
        ]