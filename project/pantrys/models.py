from django.db import models
from django.contrib.auth.models import User
from project.recipes.models import Food

class UserIngredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=8, null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{} {}".format(self.food, self.user)