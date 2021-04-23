from django.conf import settings
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
    scientific_name = models.CharField(max_length=32, unique=True)                       
    description = models.CharField(max_length=255)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through="UserFood")

    def __str__(self):
        return "Food %s: %s" % (self.fd_id, self.scientific_name) 

class UserFood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    in_pantry = models.BooleanField(default=True)
    
    def __str__(self):
        return "%s has %sx %s" % (self.user.username, self.qty, self.food.scientific_name)
    
    class Meta:
        unique_together = [["user", "food", "in_pantry"]]

