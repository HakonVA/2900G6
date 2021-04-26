from django.urls import include, path

from .views import (
    loginpage,
    signuppage,
    logoutpage,
    logmeout,
)

urlpatterns = [
    path('login', view=loginpage, name="login"),
    path('signup', view=signuppage, name="signup"),
    path('logoutpage', view=logoutpage, name='logoutpage'),
    path('logmeout', view=logmeout, name="logmeout"),
]   