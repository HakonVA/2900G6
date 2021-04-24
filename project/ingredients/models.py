from django.contrib.auth.models import User
from django.db import models

class Food(models.Model):
    """
    The Food table contains the excepted food items (ingredients)

        fd_id               | The unique permanent identifier of the food item
        fd_category         | The category the food item belongs to; protein, fruit, vegetable, dairy and fat
        scientific_name     | The scientific name of the food item
    """
    FOOD_CATEGORY = [
        ("0", "protein"),
        ("1", "fruit"),
        ("2", "vegetable"),
        ("3", "dairy"),
        ("4", "fat"),
    ]

    fd_id = models.AutoField(primary_key=True)  
    scientific_name = models.CharField(max_length=32)                       
    category = models.CharField(max_length=32, choices=FOOD_CATEGORY, default=None)                        

    def __str__(self):
        return "%s" % (self.scientific_name) 

class Pantry(models.Model):
    """
    The Pantry table contains the user ingredients 
    
        name                | The name for the food item
        user                | Unique permanent identifier for the specific user

        amount              | Amount of food item in grams, unite, quantity (*)
        expiration_date     | The expiration date for the food item (*)
    """
    py_id = models.AutoField(auto_created=True, primary_key=True, serialize=False) 
    name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user, self.name) 
