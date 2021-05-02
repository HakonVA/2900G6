from django.db import models
from django.contrib.auth.models import User
from project.recipes.models import Food, Recipe

class ShoppingEntry(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.RESTRICT, null=True, blank=True)
    unit = models.CharField(max_length=8, null=True, blank=True)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=True, blank=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return "ShoppingEntry: {} {}".format(self.name, self.food)

class ShoppingList(models.Model):
    recipes = models.ManyToManyField(Recipe, blank=True)
    entries = models.ManyToManyField(ShoppingEntry, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Shopping: {} {} {}".format(self.recipes, self.entries, self.user)