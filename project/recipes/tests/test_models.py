from django.test import TestCase
from project.recipes.models import Food, Ingredient, Recipe

class FoodTest(TestCase):

    def test_create_food(self):
        
        new_food = Food.objects.create(name="fish")
        new_food.full_clean()
        assert(new_food.name == "fish")

    def test_max_length(self):
        
        long_name="fish"*20
        max_length_name = 64
        assert(len(long_name)>max_length_name)
        new_food = Food.objects.create(name=long_name)
        try:
            #if this passes, assertion error is called
            new_food.full_clean()
        except:
            pass

    def test_upper_case(self):

        new_food = Food.objects.create(name="FISH")
        new_food.full_clean()
        assert(new_food.name == "fish")

    #TODO:
    #food tests with weird letters?


class IngredientTest(TestCase):
    
    #helper method
    def create_food(self,food_name):
        new_food = Food.objects.create(name=food_name)
        new_food.full_clean()
        return new_food

    def test_food_ingredient(self):
        pass
    
    def test_amount_negative(self):

        torsk = self.create_food("torsk")

        neg_value = -5

        new_ingredient = Ingredient.objects.create(food=torsk, amount = neg_value)
        new_ingredient.full_clean()

        assert(new_ingredient.amount >= 0)        

    def test_amount_mixed(self):

        skrei = self.create_food("skrei")

        mixed_amount = "5ab3"
        
        try:
            new_ingredient = Ingredient.objects.create(food=skrei, amount = mixed_amount)
        except:
            pass

    def test_amount_length(self):
        
        makrell = self.create_food("makrell")
        makrell_long = 5555555555

        try:
            new_ingredient = Ingredient.objects.create(food=makrell, amount = makrell_long)
        except:
            pass

    #unit has no real limits in terms of type
    #should not be number?
    def test_unit_length(self):
        #length
        max_length = 8
        hyse = self.create_food("hyse")
        unit_length = "kilogrammer"

        try: 
            new_ingredient = Ingredient.objects.create(food=hyse, unit = unit_length)
        except:
            pass

class RecipeTest(TestCase):
    #TODO: test limits
    #test the criterias of the database values
    pass
    def test_prep_time_negative(self):
        pass
    def test_servings_negative(self):
        pass
