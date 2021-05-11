from django.test import TestCase
from django.test import Client #no running server needed

#method to create a user with given name and password for a client
def createUser(client, name, passwd):
    login_attempt = client.post('/signup', {'username': name, 'password1':passwd, 'password2':passwd })
    return login_attempt.status_code

class CreateUserTest(TestCase):
    
    #signup
    def test_regular_user(self):
        username_signup = "TestUser"
        password_signup = "Hallo123@"

        c = Client()

        response = c.post('/signup', {'username': username_signup, 'password1':password_signup, 'password2':password_signup })

        assert(response.status_code == 302)

    #test to create two of the same name
    def test_duplicate_user(self):
        username_signup = "TestUser"
        password_signup = "Hallo123@"

        #create user
        c = Client()
        response = c.post('/signup', {'username': username_signup, 'password1':password_signup, 'password2':password_signup })
        assert(response.status_code == 302)

        #logout
        c.get('/logoutpage')
        logout_response = c.get('/logmeout')
        assert(logout_response.status_code == 302)

        #create duplicate
        duplicate_response = c.post('/signup', {'username': username_signup, 'password1':password_signup, 'password2':password_signup })
        assert(duplicate_response != 302)

    #wrong password should not create a 302
    def test_wrong_password(self):
        username_signup     = "TestUser"
        password1_signup    = "Hallo123@"
        password2_signup    = "Hallo123"

        c = Client()

        response = c.post('/signup', {'username': username_signup, 'password1':password1_signup, 'password2':password2_signup })
        assert(response.status_code != 302)

    #test to see if login works with user
    def test_login(self):
        username_login  = "TestUser"
        password_login  = "Hallo123@"

        c = Client()

        createUser(c, username_login, password_login)

        #logout after creating a user, and logging back in
        c.get('/logmeout')

        response = c.post('/login', {'username': username_login, 'password': password_login})
        
        assert(response.status_code == 302)

    #log in, then logout, then assert template logout page
    def test_logout(self):
        #if possible to assert logoutpage after logout
            #logout = failed
        #else its good

        username_login  = "TestUser"
        password_login  = "Hallo123@"

        c = Client()

        createUser(c, username_login, password_login)

        logout_response = c.get('/logmeout')
        assert(logout_response.status_code == 302)

        logout_response = c.get('/logoutpage')

        assert(logout_response.url == '/login')

    def test_login_redirect_logoutpage(self):
        username_login  = "TestUser"
        password_login  = "Hallo123@"

        c = Client()

        createUser(c, username_login, password_login)

        login_response = c.get('/login')
        assert(login_response.url == '/logoutpage')
    
    def test_signup_redirect_logoutpage(self):
        username_login  = "TestUser"
        password_login  = "Hallo123@"

        c = Client()

        createUser(c, username_login, password_login)

        login_response = c.get('/signup')
        assert(login_response.url == '/logoutpage')
    