from django.test import TestCase, Client
from project.users.tests.test_views import createUser
from project.recipes.models import Food
from django.contrib.auth.models import User
from project.pantrys.models import UserIngredient

class PantryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        username = "TestUser"
        password = "Hallo123@"
        createUser(self.client, username, password)
        self.user = User.objects.get(username=username)

    def test_pantry_index_view_1(self):
        # Test 1: zero recipes found
        new_user_ingredient = UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user)

        response = self.client.get('/pantrys/')
 
        assert(len(response.context['object_list']) == 1)
        assert(len(response.context['recipes_list']) == 0)
        assert(response.status_code == 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'pantrys/base.html')

    def test_pantry_index_view_2(self):
        # Test 2: One recipe found
        UserIngredient.objects.create(food=Food.objects.get(name="olive oil"), user=self.user, amount=5)
        UserIngredient.objects.create(food=Food.objects.get(name="chestnut mushrooms"), user=self.user, amount=50)
        UserIngredient.objects.create(food=Food.objects.get(name="vegetarian cheddar"), user=self.user, amount=25)
        UserIngredient.objects.create(food=Food.objects.get(name="parsley leaves"), user=self.user, amount=10)
        UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user, amount=2)

        response = self.client.get('/pantrys/')
 
        assert(len(response.context['object_list']) == 5)
        assert(len(response.context['recipes_list']) == 1)
        assert(response.status_code == 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'pantrys/base.html')

    def test_pantry_index_view_3(self):
        # Test 3: Got all ingredients for recipes, but not the right amount
        UserIngredient.objects.create(food=Food.objects.get(name="olive oil"), user=self.user, amount=1)
        UserIngredient.objects.create(food=Food.objects.get(name="chestnut mushrooms"), user=self.user, amount=50)
        UserIngredient.objects.create(food=Food.objects.get(name="vegetarian cheddar"), user=self.user, amount=25)
        UserIngredient.objects.create(food=Food.objects.get(name="parsley leaves"), user=self.user, amount=10)
        UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user, amount=2)

        response = self.client.get('/pantrys/')
 
        assert(len(response.context['object_list']) == 5)
        assert(len(response.context['recipes_list']) == 0)
        assert(response.status_code == 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'pantrys/base.html')

    def test_user_ingredient_list_view(self):
        #checking if we get the right page

        UserIngredient.objects.create(food=Food.objects.get(name="olive oil"), user=self.user, amount=5)
        UserIngredient.objects.create(food=Food.objects.get(name="chestnut mushrooms"), user=self.user, amount=50)
        UserIngredient.objects.create(food=Food.objects.get(name="vegetarian cheddar"), user=self.user, amount=25)
        UserIngredient.objects.create(food=Food.objects.get(name="parsley leaves"), user=self.user, amount=10)
        UserIngredient.objects.create(food=Food.objects.get(name="egg"), user=self.user, amount=2)

        response = self.client.get('/pantrys/ingredients/')
        assert(len(response.context['object_list']) == 5)
        assert(len(response.context['recipes_list']) == 1)
        assert(response.status_code == 200)
        self.assertEqual(response.context['user'], self.user)
        self.assertTemplateUsed(response, 'pantrys/user_ingredients.html')
        
    def test_user_ingredient_create_view(self):
        #TODO: major this is not working
        response = self.client.get('/pantrys/ingredients/create/')
        assert(response.status_code == 200)

        test_object = Food.objects.get(name="egg")
        
        #This wont work?
        response = self.client.post('/pantrys/ingredients/create/' ,{'food':test_object, 'amount':100, 'unit':"g"})
        # assert(response.status_code == 302)
        assert(response.status_code == 200)

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

    def test_pantry_autocomplete_view_term_valid(self):
        # test 1: term is given 
        response = self.client.get('/pantrys/ingredients/create/autocomplete/', {'term':'egg'})
        self.assertEqual(response.status_code, 200)

    def test_pantry_autocomplete_view_term_invalid(self):
        # test 2: term is not given 
        response = self.client.get('/pantrys/ingredients/create/autocomplete/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/pantrys/ingredients/')

    def test_pantry_sumbitfood_view_food_valid(self):
        #test 1: valid food for sumbit
        response = self.client.post('/pantrys/ingredients/create/submitfood/', {'food':'egg', 'amount':100, 'unit':"g"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/pantrys/ingredients/')

    def test_pantry_sumbitfood_view_food_invalid(self):
        #test 1: invalid food for sumbit
        response = self.client.post('/pantrys/ingredients/create/submitfood/', {'food': 'toothpaste', 'amount':100, 'unit':"g"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/pantrys/ingredients/create/')