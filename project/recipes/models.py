from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Food(models.Model):

    name = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Ingredient(models.Model):

    food = models.ForeignKey(Food, on_delete=models.RESTRICT)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, validators=[MinValueValidator(0.0)], null=True, blank=True)
    unit = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.amount, self.unit, self.food)

class Recipe(models.Model):
    """[summary]

    Fields:
        name            | The recipe name
        description     | The description for the recipe
        rating          | The rating for the recipe (0 out 5 stars) 
        prep_time       | The preparation time for the recipe (in minutes)
        instruction     | The instructions to complete recipe
        servings        | The servings size of the recipe (number of people)
        image           | The recipe image 
        link            | The recipe link∕URL if fetched from a website 
        ingredients     | A ManyToManyField to recipe ingredients
        data_created    | The date/time the recipe was created
    
    """

    name = models.CharField(max_length=64)
    description = models.TextField(default='', blank=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    prep_time = models.IntegerField(default=0)
    instruction = models.TextField(default='', blank=True) 
    servings = models.IntegerField(default=1)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True, default='default.png')
    link = models.URLField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

