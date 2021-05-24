from django.test import TestCase, Client
from django.urls import reverse
from project.users.tests.test_views import createUser
from project.recipes.models import Food

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
        response = self.client.get(reverse('pantrys:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pantrys/create_form.html')

    def test_ingredients_update_url(self):
        food_item = Food.objects.get(name = "egg")
        response = self.client.post('/pantrys/ingredients/create/submitfood/', {'food':food_item, 'amount':100, 'unit':"g"})
        
        response = self.client.post('/pantrys/ingredients/1/update/',{'food':Food.objects.get(name="egg"),'amount':500, 'unit':"g"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pantrys/update_form.html')

    def test_ingredients_delete_url(self):
        food_item = Food.objects.get(name = "egg")
        response = self.client.post('/pantrys/ingredients/create/submitfood/', {'food':food_item, 'amount':100, 'unit':"g"})
        
        response = self.client.get('/pantrys/ingredients/1/delete/')
        self.assertTemplateUsed(response, 'pantrys/delete_form.html')

        response = self.client.post('/pantrys/ingredients/1/delete/')
        self.assertEqual(response.status_code, 302)

    def test_ingredients_autocomplete_url(self):
        #TODO:
        pass

    def test_ingredients_sumbitfood_url(self):
        #TODO:
        pass