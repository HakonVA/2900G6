from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

#render homepage
def homepage(request):
    return render(request, 'home.html')

def loginpage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            # Invalid login. Tell user.
            print("---LOGIN ATTEMPT FAILED ---")
            pass
    else:
        form = AuthenticationForm()
    return render(request, 'pages/loginpage.html', {'form': form})

def signuppage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signuppage.html', {'form': form})

#hompepage view?

#since login and ingredients have their own view