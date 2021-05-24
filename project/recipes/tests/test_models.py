from django.test import TestCase
from project.recipes.models import Food, Ingredient, Recipe
from django.core.exceptions import ValidationError

class FoodTest(TestCase):

    def test_food_create_food(self):
        
        new_food = Food.objects.create(name="fish")
        new_food.full_clean()
        assert(new_food.name == "fish")


    def test_food_max_length(self):
        
        long_name="fish"*20
        max_length_name = 64
        assert(len(long_name)>max_length_name)
        new_food = Food.objects.create(name=long_name)
        try:
            #if this passes, assertion error is called
            new_food.full_clean()
        except:
            pass

    def test_food_str(self):
        food_name = "fish"
        new_food = Food.objects.create(name=food_name)
        new_food.full_clean()

        valid_representation = f"{new_food}"

        self.assertEqual(str(new_food), valid_representation)

    def test_food_uppercase_save(self):
        new_food = Food.objects.create(name="FISH")
        new_food.full_clean()
        assert(new_food.name == "fish")

    def test_food_lowercase_save(self):
        new_food = Food.objects.create(name="fish")
        new_food.full_clean()
        self.assertEqual(new_food.name, "fish")

    def test_food_randomcase_save(self):
        new_food = Food.objects.create(name="fIsH")
        new_food.full_clean()
        self.assertEqual(new_food.name, "fish")

    #TODO:
    #food tests with weird letters?

class IngredientTest(TestCase):
    #helper method
    def create_food(self,food_name):
        new_food = Food.objects.create(name=food_name)
        new_food.full_clean()
        return new_food
    
    def test_ingredient_str(self):
        food_name = "fish"

        new_food = Food.objects.create(name=food_name)
        amount = 250
        unit = 'g'
        new_ingredient = Ingredient(food=new_food, amount=amount, unit=unit)

        valid_representation = f"{amount} {unit} {new_food}"

        self.assertEqual(str(new_ingredient), valid_representation)
    
    def test_ingredient_amount_negative(self):
        torsk = self.create_food("torsk")
        try:
            new_ingredient = Ingredient.objects.create(food=torsk, amount=-5)
            new_ingredient.full_clean()
        except ValidationError:
            pass

    def test_ingredient_amount_mixed(self):

        skrei = self.create_food("skrei")

        mixed_amount = "5ab3"
        
        try:
            new_ingredient = Ingredient.objects.create(food=skrei, amount=mixed_amount)
        except:
            pass

    def test_ingredient_amount_max_length(self):
        
        makrell = self.create_food("makrell")
        makrell_long = 5555555555

        try:
            new_ingredient = Ingredient.objects.create(food=makrell, amount=makrell_long)
        except:
            pass

    def test_ingredient_unit_length(self):
        #unit has no real limits in terms of type
        #should not be number?
        
        #length
        max_length = 8
        hyse = self.create_food("hyse")
        unit_length = "kilogrammer"

        try: 
            new_ingredient = Ingredient.objects.create(food=hyse, unit=unit_length)
        except:
            pass

class RecipeTest(TestCase):
    
    #helper method
    def create_food(self,food_name):
        new_food = Food.objects.create(name=food_name)
        new_food.full_clean()
        return new_food
    
    #helper method
    def create_ingredient(self, food_name, amount, unit):
        new_food = self.create_food(food_name)
        new_ingredient = Ingredient.objects.create(food=new_food, amount=amount, unit=unit)
        new_ingredient.full_clean()
        return new_ingredient

    def test_recipe_str(self):
        recipe_name = "Recipe name"
        new_recipe = Recipe(name=recipe_name)
        valid_representation = f"{recipe_name}"

        self.assertEqual(str(new_recipe), valid_representation)

    def test_recipe_rating_min(self):
        # min = 0
        recipe_name = "Recipe name"
        try:
            new_recipe = Recipe(name=recipe_name, rating=-1)
            new_recipe.full_clean()
        except ValidationError:
            pass

    def test_recipe_rating_max(self):
        # max = 5
        recipe_name = "Recipe name"
        try:
            new_recipe = Recipe(name=recipe_name, rating=6)
            new_recipe.full_clean()
        except ValidationError:
            pass

    def test_recipe_prep_time_min(self):
        #test the criterias of the database values
        recipe_name = "Recipe name"
        try:
            new_recipe = Recipe(name=recipe_name, prep_time=-1)
            new_recipe.full_clean()
        except ValidationError:
            pass
        
    def test_recipe_servings_min(self):
        #test the criterias of the database values
        recipe_name = "Recipe name"
        try:
            new_recipe = Recipe(name=recipe_name, prep_time=-1)
            new_recipe.full_clean()
        except ValidationError:
            pass
   
    def test_recipe_name(self):
        #recipe needs food and ingredient
        abbor = self.create_ingredient("abbor", 100, "g")
        fiskekaker = Recipe.objects.create(name="fiskekaker")
        fiskekaker.ingredients.add(abbor)
        fiskekaker.full_clean()
        assert(str(fiskekaker) == "fiskekaker")