from django.contrib.auth.models import User
from django.db import models

class Food(models.Model):
    """
    Food                    | The known and accepted food items
        fd_id               | Unique permanent identifier of the food
        fd_category         | Food category the food belongs to (protein, fruit, vegetable, dairy, fat)
        scientific_name     | The scientific name for the food
        description         | Description of the food
    """
    FOOD_CATEGORY = [
        ("0", "protein"),
        ("1", "fruit"),
        ("2", "vegetable"),
        ("3", "dairy"),
        ("4", "fat"),
    ]

    fd_id = models.AutoField(primary_key=True)  
    fd_category = models.CharField(max_length=32, choices=FOOD_CATEGORY, default=None)                        
    scientific_name = models.CharField(max_length=32)                       

    def __str__(self):
        return "fd_id:%s fd_category%s scientific_name:%s" % (self.fd_id, self.fd_category, self.scientific_name) 

class User_Food(models.Model):
    """
    User Food
        amount              | The users amount in grams or unites
        fd_id               | Unique permanent identifier of the food
        user                | Unique permanent identifier for specific user
    """
                      
    # amount = models.CharField(max_length=32, null=True)                   
    name = models.CharField(max_length=32)
    fd_id = models.ForeignKey(Food, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.user, self.fd_id) 


# class Food_nutrient(models.Model):
#     """
#     Food_nutrient
#         id                  
#         fd_id               | ID of the food this food nutrient pertains to
#         amount/unit         | Amount of the nutrient per 100g of food. Specified i n unit defined in the nutrient table.
#         protein_value       | The factor for protein
#         fat_value           | The factor for fat
#         carbohydrate_value  | The factor for carbohydrates
#     """
#     fd_id = models.ForeignKey(Food, on_delete=models.CASCADE)
#     amount = models.CharField(max_length=32)
#     protein_value = models.CharField(max_length=32)
#     fat_value = models.CharField(max_length=32)
#     carbohydrate_value = models.CharField(max_length=32)
    
#     def __str__(self):
#         return "prot: %s fat: %s carb: %s" % (self.protein_value, self.fat_value, self.carbohydrate_value)