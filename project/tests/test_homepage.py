from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

homepage_title = "Project Name" #the project name, update when changed

class HomepageTest(TestCase):
    #test for asserting that we are using the homepage template
    def test_homepage(self):
        response = self.client.get(f'')
        self.assertTemplateUsed(response, 'pages/home.html')

class VisitPageTest(StaticLiveServerTestCase):
    #tests for asserting that the homepage has the correct information
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(f'{self.live_server_url}')
        self.homepage_url = self.live_server_url

    def tearDown(self):
        self.browser.quit()
    
    def test_homepage_title(self):
        self.assertEqual(self.browser.title, homepage_title)

    def test_button_login(self):
        
        login_button = self.browser.find_element_by_class_name("Login")
        
        login_button.send_keys(Keys.ENTER)

        self.assertEqual(f'{self.homepage_url}/login', self.live_server_url)

    def test_button_ingredients(self):
        
        ingredients_button = self.browser.find_element_by_class_name("Ingredients")

        ingredients_button.send_keys(Keys.ENTER)

        self.assertEqual(f'{self.homepage_url}/ingredients', self.live_server_url)

