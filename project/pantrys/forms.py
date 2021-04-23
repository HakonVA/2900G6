from django import forms
from crispy_forms.helper import FormHelper

from .models import (
    UserIngredient,
)

class PantryCreateForm(forms.ModelForm):
    class Meta:
        model = UserIngredient
        fields = [
            'food',
            'amount',
            'unit'
        ]