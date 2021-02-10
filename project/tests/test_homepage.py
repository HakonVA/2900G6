from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium import webdriver

homepage_title = "Homepage" #used to determine if homepage is built correctly

#import info for tests, all methods need test_.. etc in the name

class HomepageTest(TestCase):
    
    #test for asserting that we are using the homepage template
    def test_homepage(self):
        response = self.client.get(f'')
        self.assertTemplateUsed(response, 'pages/home.html')

class VisitPageTest(StaticLiveServerTestCase):
    #test for asserting that the homepage title is correct
    def test_homepage_title(self):

        #running on ubuntu terminal, no display        
        browser = webdriver.Firefox()

        browser.get(f'{self.live_server_url}')

        browser.quit()




        

#assert that homepage has title "homepage"
#find title
#with views?


