from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config.urls import urlpatterns



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

    def test_homepage_visitor(self):

        #currently supported pages from homepage:
        self.supported_pages = [ "login", "signup", "ingredients", "recipes"]
        self.supported_pages = [ "login", "signup", "ingredients", "recipes"]

        #fetch hrefs for these, and check if redirect or 404?

        for page in self.supported_pages:
            try:
                page_found = self.browser.find_element_by_id(page)
                #press enter? check url to pages supported pages
                print("did find:", page)
                print(page_found)
            except:
                print("did not find:", page)

        #if we fetch something that is currently not supported, an error should apply
        #if not the page is in development

    def test_homepage_user(self):
        pass



    
