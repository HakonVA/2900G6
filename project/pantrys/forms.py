from django import forms
from crispy_forms.helper import FormHelper

from .models import (
    UserIngredient,
)

class PantryForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = [
            'food',
            'amount',
            'unit'
        ]