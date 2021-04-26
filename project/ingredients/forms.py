from django.forms import ModelForm

from .models import (
    Food,
    Pantry,
)

class PantryForm(ModelForm):
    class Meta:
        model = Pantry
        fields = [
            'name',
        ]

class FoodUpdateForm(ModelForm):
    pass

class FoodDeleteForm(ModelForm):
    pass
        
