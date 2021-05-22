from django.test import TestCase
from django.test import Client
from project.recipes.models import Food
from django.contrib.auth.models import User
from project.users.tests.test_views import createUser
from project.pantrys.models import UserIngredient
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError

class PantryModelTest(TestCase):
    def setUp(self):
        c = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(c, username, password)

        self.user = User.objects.get(username=username)

    def test_user_ingredient_str(self):
        #need food and a user
        food_test = Food.objects.get(name="egg")
        amount = 10
        unit = "pcs"

        new_user_ingredient = UserIngredient.objects.create(food=food_test, user=self.user, amount=amount, unit=unit)

        valid_representation = f"{amount} {unit} {food_test} {self.user}"

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

    def test_user_ingredient_duplicates_entries(self):
        try:
            new_user_ingredient = UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user, amount=5)
            new_user_ingredient_2 = UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user, amount=10)
        except IntegrityError:
            pass

    def test_user_ingredient_negative_amount(self):
        try:
            new_user_ingredient = UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user, amount=-5)
            new_user_ingredient.full_clean()
        except ValidationError:
            pass