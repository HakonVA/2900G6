from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class RedirectTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)