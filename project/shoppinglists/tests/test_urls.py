from django.test import TestCase, Client
from project.users.tests.test_views import createUser

class ShoppingUrlTest(TestCase):
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

    def test_shopping_list_url(self):
        response = self.client.get('/shopping/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglists/base.html')

    def test_shopping_create_url(self):
        response = self.client.get('/shopping/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglists/create_form.html')

    def test_shopping_update_url(self):
        response = self.client.post('/shopping/create', {'name': "test", 'unit': "g", 'amount': 10})

        response = self.client.get('/shopping/1/update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglists/update_form.html')

    def test_shopping_delete_url(self):
        response = self.client.post('/shopping/create', {'name': "test", 'unit': "g", 'amount': 10})

        response = self.client.get('/shopping/1/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglists/delete_form.html')
        
    def test_shopping_checkout_url(self):
        #TODO: ???
        pass