from django.test import TestCase, Client
from project.users.tests.test_views import createUser

class RecipeUrlTest(TestCase):
    def setUp(self):
        self.client = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(self.client, username, password)

    def test_templates_logged_out(self):
        #TODO: ???
        pass        

    def test_templates_logged_in(self):
        #TODO: ???
        pass

    def test_recipe_list_url(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    def test_recipe_detail_url(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_detail.html')
    
    def test_recipe_to_shopping_url(self):
        response = self.client.get('/recipes/1/add_to_shopping/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/shopping/')