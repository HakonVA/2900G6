from django.db import models

class Food(models.Model):
    """
    Food
        fd_id               | Unique permanent identifier of the food
        fd_category_id      | Id of the food category the food belongs to
        scientific_name     | The scientific name for the food
        description         | Description of the food
    """
    fd_id = models.AutoField(primary_key=True)  
    fd_category_id = models.CharField(max_length=32)                        
    scientific_name = models.CharField(max_length=32)                       
    description = models.CharField(max_length=255)  

    def __str__(self):
        return "fd_id: %s name: %s" % (self.fd_id, self.scientific_name) 



# class User_Food(models.Model):
#     """
#     Food
#         fd_id               | Unique permanent identifier of the food
#         fd_category_id      | Id of the food category the food belongs to
#         scientific_name     | The scientific name for the food
#         description         | Description of the food
#     """
#     fd_id = models.AutoField(primary_key=True)  
#     fd_category_id = models.CharField(max_length=32)                        
#     name = models.CharField(max_length=32)                       
#     description = models.CharField(max_length=255)  

#     def __str__(self):
#         return "fd_id: %s name: %s" % (self.fd_id, self.scientific_name) 



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








