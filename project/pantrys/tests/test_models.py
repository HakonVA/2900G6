from django.test import TestCase
from django.test import Client
from project.recipes.models import Food
from django.contrib.auth.models import User
from project.users.tests.test_views import createUser
from project.pantrys.models import UserIngredient
from django.core.exceptions import ObjectDoesNotExist


class PantryModelTest(TestCase):
    def setUp(self):
        c = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(c, username, password)

        self.user = User.objects.get(username=username)

    def test_user_ingredient(self):
        #need food and a user
        food_test = Food.objects.get(name="egg")

        new_user_ingredient = UserIngredient.objects.create(food=food_test, user=self.user)

        valid_representation = f"{food_test} 0 {None} {self.user}"

        assert(str(new_user_ingredient) == valid_representation)        
        
    def test_user_ingredient_valid_food(self):
        food_name = "egg"
        food_test = Food.objects.get(name=food_name)

        new_user_ingredient = UserIngredient.objects.create(food=food_test, user=self.user)
        self.assertEqual(new_user_ingredient.food.name, food_name)
        self.assertEqual(new_user_ingredient.user, self.user)

    def test_user_ingredient_invalid_food(self):
        food_name = "toothpaste"
        try:
            food_test = Food.objects.get(name=food_name)
        except ObjectDoesNotExist:
            pass