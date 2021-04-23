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
<<<<<<< HEAD
        ]

class FoodUpdateForm(ModelForm):
    pass

class FoodDeleteForm(ModelForm):
    pass
=======
        ]
>>>>>>> origin/recipes
