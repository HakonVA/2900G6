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

    def page_on_id(self, id_name, html_page):
        
        element_found = self.browser.find_element_by_id(id_name)
        
        #click href
        response = element_found.click()
        
        self.assertTemplateUsed(response, html_page)

    def test_homepage_pages_standard(self):

        #currently supported pages from homepage:
        homepage_standard = ["ingredients", "recipes", "home", "login",
                            "signup"]

        static_pages = {"ingredients": "pages/ingredients.html", 
                        "recipes": "pages/recipes.html",
                        "home": "pages/home.html",
                        "login": "pages/loginpage.html",
                        "signup": "pages/signuppage.html",}

        for page in homepage_standard:
            self.browser.get(f'{self.homepage_url}')
            self.page_on_id(page, static_pages[page])

    def test_signup(self):

        username_ff = "EliasElias"
        password_ff = "DN6T5DDMdi7m2ee"

        self.browser.get(f'{self.homepage_url}/signup')

        self.browser.find_element_by_id("id_username").send_keys(username_ff)

        self.browser.find_element_by_id("id_password1").send_keys(password_ff)

        self.browser.find_element_by_id("id_password2").send_keys(password_ff)

        self.browser.find_element_by_id("submit_signup").click()

        logout_element = self.browser.find_element_by_id("logout")

        response = logout_element.click()

        self.assertTemplateUsed(response, "pages/logoutpage.html")
