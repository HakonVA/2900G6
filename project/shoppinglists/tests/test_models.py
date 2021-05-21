from django.test import TestCase
from project.shoppinglists.models import Shopping
from django.contrib.auth.models import User

class TestShoppingModel(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username="TestUser", password="Hallo123@")
        self.new_user.save()

    def test_shopping_lowercase_save(self):
        shopping_name = "fiskekake"
        new_shopping = Shopping.objects.create(name=shopping_name, user=self.new_user)
        new_shopping.full_clean()
        new_shopping.save()       
         
        self.assertEqual(new_shopping.name, shopping_name)
        self.assertEqual(new_shopping.user, self.new_user)
    
    def test_shopping_uppercase_save(self):
        shopping_name = "FISKEKAKE"
        new_shopping = Shopping.objects.create(name=shopping_name, user=self.new_user)
        new_shopping.full_clean()
        new_shopping.save()        

        self.assertEqual(new_shopping.name, shopping_name.lower())
        self.assertEqual(new_shopping.user, self.new_user)

    def test_shopping_randomcase_save(self):
        shopping_name = "FiSkEkAkE"
        new_shopping = Shopping.objects.create(name=shopping_name, user=self.new_user)
        new_shopping.full_clean()
        new_shopping.save()

        self.assertEqual(new_shopping.name, shopping_name.lower())
        self.assertEqual(new_shopping.user, self.new_user)        
    
    def test_shopping_str(self):
        shopping_name = "fiskekake"
        shopping_amount = 100
        shopping_unit = 'g'
        new_shopping = Shopping.objects.create(name=shopping_name, unit=shopping_unit,
                                               amount=shopping_amount,user=self.new_user)
        new_shopping.full_clean()
        new_shopping.save()   

        valid_representation = f'{shopping_amount} {shopping_unit} {shopping_name} {self.new_user}'
        assert(str(new_shopping) == valid_representation)

    def test_shopping_name_max_length(self):
        #TODO:
        pass

    def test_shopping_unit_max_length(self):
        #TODO:
        pass 