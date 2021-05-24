from django.test import TestCase
from django.test import Client
from project.users.tests.test_views import createUser
from project.recipes.models import Food
from django.contrib.auth.models import User
from project.pantrys.models import UserIngredient

class TestViewsPantry(TestCase):
    def setUp(self):
        self.client = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(self.client, username, password)
        self.user = User.objects.get(username=username)

    #checking if get the right page
    def test_pantry_index_view(self):
        new_user_ingredient = UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user)

        response = self.client.get('/pantrys/')
 
        assert(len(response.context['object_list']) == 1)
        assert(len(response.context['recipes_list']) == 0)
        assert(response.status_code == 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'pantrys/base.html')

    #checking if we get the right page
    def test_user_ingredient_list_view(self):
        #TODO: Make it so recipes is found 1 
        response = self.client.get('/pantrys/ingredients/')

        assert(len(response.context['object_list']) == 0)
        assert(len(response.context['recipes_list']) == 0)
        assert(response.status_code == 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'pantrys/user_ingredients.html')
        
    def test_user_ingredient_create_view(self):
        #TODO: major

        response = self.client.get('/pantrys/ingredients/create/')
        assert(response.status_code == 200)

        test_object = Food.objects.get(name="egg")
        
        #This wont work?
        response = self.client.post('/pantrys/ingredients/create/' ,{'food':test_object, 'amount':100, 'unit':"g"})
        assert(response.status_code == 302)

    def test_user_ingredient_update_view(self):
        response = self.client.get('/pantrys/')
        assert(response.status_code == 200)

        #post egg
        food_item = Food.objects.get(name = "egg")

        response = self.client.post('/pantrys/ingredients/create/submitfood/', {'food':food_item, 'amount':100, 'unit':"g"})
        
        response = self.client.get('/pantrys/ingredients/1/update/')
        assert(response.status_code == 200)

        response = self.client.post('/pantrys/ingredients/1/update/',{'food':Food.objects.get(name="egg"),'amount':500, 'unit':"g"})
        update_object = response.context['object']

        assert(update_object.food.name == "egg")
        assert(update_object.unit == "g")
        assert(update_object.amount == 500)

    def test_user_ingredient_delete_view(self):
        
        response = self.client.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 0)

        food_item = Food.objects.get(name="egg")
        self.client.post('/pantrys/ingredients/create/submitfood/', {'food':food_item, 'amount':100, 'unit':"g"})

        response = self.client.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 1)

        response = self.client.get('/pantrys/ingredients/1/delete/')
        assert(response.status_code == 200)
        
        response = self.client.post('/pantrys/ingredients/1/delete/')
        assert(response.status_code == 302)

        response = self.client.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 0)




    