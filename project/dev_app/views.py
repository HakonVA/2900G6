from django.shortcuts import render

# Create your views here.

#render homepage
def homepage(request):
    return render(request, 'home.html')

#hompepage view?

#since login and ingredients have their own view