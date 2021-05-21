from django.test import TestCase
from django.test import Client
from project.users.tests.test_views import createUser
from project.recipes.models import Food

class TestViewsPantry(TestCase):
    # def setUp(self):
    #     self.client = Client()
    #     username = "TestUser"
    #     password = "Hallo123@"
    #     createUser(self.client, username, password)

    #checking if get the right page
    def test_pantry_index_view(self):

        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/pantrys/')
        
        assert(len(response.context['recipes_list']) == 0)
        assert(response.status_code == 200)

    #checking if we get the right page
    def test_user_ingredient_list_view(self):

        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/pantrys/ingredients/')

        assert(len(response.context['recipes_list']) == 0)
        assert(response.status_code == 200)
        
    def test_user_ingredient_create_view(self):

        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/pantrys/ingredients/create/')
        assert(response.status_code == 200)

        # response = c.post( '/pantrys/ingredients/create/' ,{"food":, "amount":2, "unit":"pcs"})
        #print(response)
        response = c.get('/pantrys/')

        #print(response.context)

        assert(len(response.context['recipes_list']) == 1)
        assert(response.context['recipes_list'][0].name == "egg")

    def test_user_ingredient_update_view(self):
        #TODO:
        pass
    
    def test_user_ingredient_delete_view(self):
        #TODO:
        pass
    