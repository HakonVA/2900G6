from django.test import TestCase
from django.core.exceptions import ValidationError

class LoginViewTest(TestCase):

    #helper method for asserting templates
    def assert_templates(self, url, template_names):
        response = self.client.get(url)
        for template in template_names:
            self.assertTemplateUsed(template)

    def test_logout_redirects_to_login(self):
        response = self.client.get("/logmeout")
        self.assertRedirects(response, "/login")

    def test_logoutpage_redirects_to_login(self):
        response = self.client.get("/logoutpage")
        self.assertRedirects(response, "/login")
    
    def test_login_uses_correct_template(self):
        templates = ["base.html", "/users/loginpage.html"]
        self.assert_templates("/login", templates)

    def test_signup_uses_correct_template(self):
        templates = ["base.html", "/users/signuppage.html"]
        self.assert_templates("/signup", templates)
        
    def test_logout_uses_correct_template(self):
        templates = ["base.html", "/users/logoutpage.html"]
        self.assert_templates("/logoutpage", templates)