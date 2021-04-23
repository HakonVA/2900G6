from django.db import models

from project.ingredients.models import Food

# Create your models here.


class Recipe(models.Model):
    rc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    foods = models.ManyToManyField(Food, through="RecipeFood")
    
    def __str__(self):
        return "Recipe %d: %s" % (self.rc_id, self.name)

class RecipeFood(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return "Rc %s needs %sx %s" % (self.recipe.name, self.qty, self.food.scientific_name)
    
    class Meta:
        unique_together = [["recipe", "food"]]