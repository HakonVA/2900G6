from django.test import TestCase
from django.test import Client
from project.users.tests.test_views import createUser
from project.shoppinglists.models import Shopping
from django.contrib.auth.models import User
from project.recipes.models import Food
from project.pantrys.models import UserIngredient 

class TestViewsShopping(TestCase):

    def test_shopping_login(self):
        #TODO:
        #for all views:
            #should not be accessible
            #without being logged inn
        pass
    
    def test_shopping_list_view(self):
        #need a user to access shopping list
        #
        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        response = c.get('/recipes/1/add_to_shopping/')
        #print(response.context)
        response = c.get('/shopping/')
        #print(response.context['object_list'])
        
        #could fetch the list we have in signals?
        #if shopping list empty
        #self.assertQuerysetEqual()

    def test_shopping_create_view(self):

        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        name = "testitem"
        unit = "g"
        amount = 10

        response = c.post('/shopping/create', {'name': name, 'unit': unit, 'amount': amount})

        assert(response.status_code == 302)

    def test_shopping_update_view(self):

        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        name = "testitem"
        unit = "g"
        amount = 10

        response = c.post('/shopping/create', {'name': name, 'unit': unit, 'amount': amount})
        
        response = c.get('/shopping/1/update/')
        
        shopping_object = response.context['object']
        assert(shopping_object.name   == name)
        assert(shopping_object.unit   == unit)
        assert(shopping_object.amount == amount)

        new_name = "testitem2"
        new_unit = "kilo"
        new_amount = 1

        response = c.post('/shopping/1/update/', {'name':new_name, 'unit':new_unit, 'amount':new_amount})

        assert(response.status_code == 302)
        response = c.get('/shopping/1/update/')

        shopping_object = response.context['object']
        assert(shopping_object.name   == new_name)
        assert(shopping_object.unit   == new_unit)
        assert(shopping_object.amount == new_amount)

    def test_shopping_delete_view(self):
        #post to delete
        #check list if object is non existent
        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        name = "testitem"
        unit = "g"
        amount = 10

        response = c.post('/shopping/create', {'name': name, 'unit': unit, 'amount': amount})
        response = c.get('/shopping/')
        
        assert(len(response.context['object_list']) == 1)

        response = c.get('/shopping/1/delete/')

        assert(response.status_code == 200)

        response = c.post('/shopping/1/delete/')

        assert(response.status_code == 302)

        response = c.get('/shopping/')

        assert(len(response.context['object_list']) == 0)

    def test_shopping_checkout(self):
        #TODO: major
        
        c = Client()
        createUser(c, "TestUser", "Hallo123@")

        #test 1: single object that we know is food

        test_name = "egg"
        test_unit = "g"
        test_amount = 100

        c.post('/shopping/create', {'name':test_name, 'unit':test_unit, 'amount':test_amount})

        response = c.post('/shopping/checkout/', {'shopping_id':1})
        print(response)
        #test 2: single object that we know is not food

        #test 3: two objects, one food, one not

        #test 4: two objects, two is food

        #test 5: two objects, two is not food

        #test 6: empty shopping

        #test 7: max_amount of items?


        #get/post shopping/checkout

        #need to check for food in database
        #vs food not in database

        #get is all
        #post is single


                

