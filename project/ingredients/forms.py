from django.forms import ModelForm
from .models import Food

class FoodCreateForm(ModelForm):
    class Meta:
        model = Food
        fields = [
            'name',
        ]

class FoodUpdateForm(ModelForm):
    pass

class FoodDeleteForm(ModelForm):
    pass
