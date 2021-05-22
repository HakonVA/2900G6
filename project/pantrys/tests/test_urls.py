from django.test import TestCase, Client
from project.users.tests.test_views import createUser
from django.urls import reverse

class PantryUrlTest(TestCase):
    def setUp(self):
        self.client = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(self.client, username, password)

    def test_pantrys_index_url(self):
        response = self.client.get(reverse('pantrys:index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pantrys/base.html')

    def test_ingredients_url(self):
        response = self.client.get(reverse('pantrys:ingredients'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pantrys/user_ingredients.html')

    def test_ingredients_create_url(self):
        #TODO:
        pass

    def test_ingredients_update_url(self):
        #TODO:
        pass

    def test_ingredients_delete_url(self):
        #TODO:
        pass