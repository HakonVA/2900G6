from django.db import models
from project.recipes.models import Food
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class UserIngredient(models.Model):
    food = models.OneToOneField(Food, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, validators=[MinValueValidator(0.0)], null=True, blank=True)
    unit = models.CharField(max_length=8, null=True, blank=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{} {} {} {}".format(self.amount, self.unit, self.food, self.user)
    
    class Meta:
        unique_together = [["food", "user"]]