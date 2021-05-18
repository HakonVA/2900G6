from django.test import TestCase
from project.shoppinglists.models import Shopping
from django.contrib.auth.models import User

class TestShoppingModels(TestCase):

    def test_save(self):
        new_user = User.objects.create(username="TestUser", password="Hallo123@")
        new_user.save()
        new_shopping = Shopping.objects.create(name="fiskekake", user=new_user)
        new_shopping.full_clean()
        new_shopping.save()        
    
    def test_str(self):
        new_user = User.objects.create(username="TestUser", password="Hallo123@")
        new_user.save()
        new_shopping = Shopping.objects.create(name="fiskekake", user=new_user)
        new_shopping.full_clean()
        new_shopping.save()   

        valid_representation = f"{new_shopping.name} {new_user.username}"
     
        assert(str(new_shopping) == valid_representation)