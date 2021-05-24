from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from project.recipes.models import Recipe
from project.recipes.models import Food
from project.recipes.models import Ingredient
from project.users.tests.test_views import createUser
from project.pantrys.models import UserIngredient

class RecipeViewTest(TestCase):

    def test_recipe_logged_out(self):
        c = Client()
        
        #if response == 200:
            #means we got to the page without
            #being logged inn

        #list view of recipies
        response = c.get('/recipes/')
        assert(response.status_code != 200)    
        
        #view a single recipe
        response = c.get('/recipes/1/')
        assert(response.status_code != 200)    
        
        #add items to shopping from recipe
        response = c.get('/recipes/1/add_to_shopping/')
        assert(response.status_code != 200)

    #same test as not logged in, with assertion of correction
    def test_recipe_logged_in(self):
        username_login  = "TestUser"
        password_login  = "Hallo123@"
        
        c = Client()

        new_user = createUser(c, username_login, password_login) #client, name, password

        response = c.get('/recipes/')
        assert(response.status_code == 200)

        response = c.get('/recipes/1/')
        assert(response.status_code == 200)

        response = c.get('/recipes/1/add_to_shopping')
        assert(response.status_code == 302 or response.status_code == 301)

    def test_recipe_detail_view(self):
        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/recipes/1/')
        self.assertTemplateUsed(response, 'recipes/recipes_detail.html')

    def test_recipe_list_view(self):
        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/recipes/')
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    #test 1:
    #empty ingredient list
    #test all added
    def test_recipe_to_shopping_list1(self):
        
        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 0)

        response = c.get('/recipes/1/add_to_shopping/')
        c.get('/shopping/checkout/')

        response = c.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 6)

    #test 2:
    #partly full ingredient list
    #test amount added is correct
    def test_recipe_to_shopping_list2(self):

        c = Client()
        createUser(c, "TestUser", "Hallo123@")
        user = User.objects.get(username="TestUser")

        response = c.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 0)

        """ 400 g cauliflower
        5 g oil
        5 g fennel seeds
        150 g red lentils
        30 g curry paste 
        20 g lemon juice """

        cauliflower_food = Food.objects.get(name="cauliflower")
        oil_food = Food.objects.get(name="oil")
        lemonjuice_food = Food.objects.get(name="lemon juice")

        #too little
        UserIngredient.objects.create(food=cauliflower_food, user=user, amount=200)
        
        #too little
        UserIngredient.objects.create(food=oil_food, user=user, amount = 2)
        
        #too much
        UserIngredient.objects.create(food=lemonjuice_food, user=user, amount = 40)

        c.get('/recipes/1/add_to_shopping/')
        c.get('/shopping/checkout/')

        response = c.get('/pantrys/ingredients/')

        response_objects = response.context['object_list']

        for objects in response_objects:
            if objects.food == "cauliflower":
                assert(objects.amount == 400)
            if objects.food == "oil":
                assert(objects.amount == 5)
            if objects.food == "lemon juice":
                assert(objects.amount == 40)









