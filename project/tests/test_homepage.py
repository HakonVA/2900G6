from django.test import TestCase

#sample test, will fail
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

class HomepageTest(TestCase):
    def returns_homepage(self):

        pass
    def returns_loginpage(self):
        pass
    def returns_ingredientpage(self):
        pass
