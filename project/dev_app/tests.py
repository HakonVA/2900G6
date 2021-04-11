from django.test import TestCase
from django.core.exceptions import ValidationError

# Create your tests here.


class LoginViewTest(TestCase):
    def test_logout_redirects_to_login(self):
        response = self.client.get("/logmeout")
        self.assertRedirects(response, "/login")
    
    def test_login_uses_correct_template(self):
        response = self.client.get("/login")
        self.assertTemplateUsed(response, "base.html")

    def test_logoutpage_redirects_to_login(self):
        response = self.client.get("/logoutpage")
        self.assertRedirects(response, "/login")