from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

homepage_title = "Fridge Friend" #the project name, update when changed

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

    