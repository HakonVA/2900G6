from django.db import models

from project.ingredients.models import Food

# Create your models here.


class Recipe(models.Model):
    rc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    req_ingredients = models.ManyToManyField(Food, related_name="req_ingredients")
    
    def __str__(self):
        return "Recipe %s: %s" % (self.rc_id, self.name)