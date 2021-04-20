"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path

from django.conf.urls import url
from project import user
#from project import user
#import project.user

from project.user.views import signuppage, loginpage, logmeout, logoutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('project.dev_app.urls')),
    path('login', user.views.loginpage, name="login"),
    path('signup', user.views.signuppage, name="signup"),
    path('logoutpage', user.views.logoutpage, name='logoutpage'),
    path('logmeout', user.views.logmeout, name="logmeout"),
    path(r'', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    path(r'info', TemplateView.as_view(template_name='pages/info.html'), name='info'),
    path('ingredients/', include('project.ingredients.urls')),
    path(r'recipes/', TemplateView.as_view(template_name='pages/recipes.html'), name='recipes'),
]
