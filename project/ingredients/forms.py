from django.forms import ModelForm
from .models import (
    Food,
    User_Food,
)

# ----------- Food forms -----------
class FoodCreateForm(ModelForm):
    class Meta:
        model = Food
        fields = [
            'scientific_name',
        ]

class FoodUpdateForm(ModelForm):
    pass

class FoodDeleteForm(ModelForm):
    pass


# ----------- User food froms -----------
class User_FoodCreateForm(ModelForm):
    class Meta:
        model = User_Food
        fields = [
            'fd_id',
        ]

class User_FoodUpdateForm(ModelForm):
    pass

class User_FoodDeleteForm(ModelForm):
    pass
