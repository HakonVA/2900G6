from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from project.recipes.models import Recipe
from project.recipes.models import Food
from project.recipes.models import Ingredient
from project.users.tests.test_views import createUser


#recipe views:

class ViewRecipiesTest(TestCase):

    def test_logged_out(self):
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
    def test_logged_in(self):
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

    #a test to view the page if missing image
    #and potenially other faults in recipes
    def test_missing_image(self):
        #TODO:
        pass
        # create a recipe without a image and see how it works
        # use setupMissing_image
        # and check if anything else will bonk it

    def test_recipe_detail_view(self):
        #TODO: major
        pass

    def test_recipe_list_view(self):
        #TODO: major
        pass

    def test_recipe_to_shopping_list(self):
        #TODO: major
        pass