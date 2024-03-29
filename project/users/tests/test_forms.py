from django.test import TestCase
from django.test import Client
from project.users.tests.test_views import createUser
import random
import string

#more edge cases for login form

class LoginFormTests(TestCase):

    #user that has been created, tries to login with wrong password
    def test_correctname_wrongpassword_login(self):
        #create a user, logout, login with wrong password

        username = "TestUser"
        password = "Hallo123@"
        wrong_password = "Hallo123"

        c = Client()
        createUser(c, username, password)
        c.get('/logmeout')

        response = c.post('/login', {'username': username, 'password': wrong_password})

        assert(response.status_code != 302)
    
    #these tests might fail, 
    def test_stringlength_username_password(self):
        # Changed in Django 3.1: The max_length increased from 30 to 150 characters.
        max_length_username = 150 + 1
        max_length_password = 4096

        username_max = "T" * max_length_username
        password_max = "@" * max_length_password
        
        assert(len(username_max) >= max_length_username)
        assert(len(password_max) >= max_length_password)

        min_length_username = 6
        min_length_password = 8

        username_min = "Test"
        password_min = "Hal123@"

        assert(len(username_min) <= min_length_username)
        assert(len(password_min) <= min_length_password)

        c = Client()

        response_code = createUser(c, username_max, password_max)
        assert(response_code != 302)
        
        response_code = createUser(c, username_min, password_min)
        assert(response_code != 302)

    def test_all_inputs_required(self):
        #test signup with just 1 password, and without username

        username_correct    = "TestUser"
        username_blank      = ""
        
        password_correct    = "Hallo123@"
        password_blank      = ""

        c = Client()

        #just the first password
        response = c.post('/signup', {'username': username_correct, 'password1':password_correct, 'password2':password_blank })
        assert(response.status_code != 302)

        #only second password
        response = c.post('/signup', {'username': username_correct, 'password1':password_blank, 'password2':password_correct })
        assert(response.status_code != 302)

        response = c.post('/signup', {'username': username_blank, 'password1':password_correct, 'password2':password_correct})
        assert(response.status_code != 302)

    def test_username_spaces(self):
        
        username_spacing            = "Test User"
        username_blank_spaced       = " "
        password_correct            = "Hallo123@"

        c = Client()

        response = createUser(c, username_spacing, password_correct)
        assert(response != 302)

        response = createUser(c, username_blank_spaced, password_correct)
        assert(response != 302)

    def test_password_space(self):

        username_correct            = "TestUser"
        password_blank_spaced       = " "

        c = Client()

        response = createUser(c, username_correct, password_blank_spaced)
        assert(response != 302)