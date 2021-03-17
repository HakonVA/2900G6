from django.forms import ModelForm

from .models import (
    Food,
    Pantry,
)

class PantryCreateForm(ModelForm):
    class Meta:
        model = Pantry
        fields = [
            'name',
        ]

class PantryDeleteForm(ModelForm):
    class Meta:
        model = Pantry
        fields = [
            'name',
        ]


