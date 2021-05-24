from django.test import TestCase
from project.shoppinglists.models import Shopping
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ShoppingModelTest(TestCase):
    def setUp(self):
        self.new_user = User.objects.create(username="TestUser", password="Hallo123@")
        self.new_user.save()

    def test_shopping_str(self):
        name = "fiskekake"
        amount = 100
        unit = 'g'

        new_shopping = Shopping.objects.create(name=name, unit=unit, amount=amount, user=self.new_user)
        new_shopping.full_clean()
        new_shopping.save()   

        valid_representation = f'{amount} {unit} {name} {self.new_user}'
        assert(str(new_shopping) == valid_representation)
        
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
    
    def test_shopping_negative_amount(self):
        try:
            new_shopping = Shopping.objects.create(name="fiskekake", amount=-5, user=self.new_user)
            new_shopping.full_clean()
        except ValidationError:
            pass

    def test_shopping_name_max_length(self):
        # max name length is 64 
        name = "a" * 65
        try:
            new_shopping = Shopping.objects.create(name=name, user=self.new_user)
            new_shopping.full_clean()
        except ValidationError:
            pass

    def test_shopping_unit_max_length(self):
        # max unit length is 8
        unit = "a" * 9
        try:
            new_shopping = Shopping.objects.create(name="fiskekake", unit=unit, user=self.new_user)
            new_shopping.full_clean()
        except ValidationError:
            pass