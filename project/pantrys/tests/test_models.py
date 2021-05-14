from django.test import TestCase
from django.test import Client
from project.recipes.models import Food
from django.contrib.auth.models import User
from project.users.tests.test_views import createUser
from project.pantrys.models import UserIngredient

class PantryModelTests(TestCase):
    
    def test_user_ingredient(self):
        #need food and a user
        c = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(c, username, password)

        user_test = User.objects.get(username=username)
        food_test = Food.objects.get(name="egg")

        new_user_ingredient = UserIngredient.objects.create(food=food_test, user=user_test)

        valid_representation = f"{food_test} {user_test}"

        assert(str(new_user_ingredient) == valid_representation)        