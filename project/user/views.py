from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def loginpage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("login")
        else:
            # Invalid login. TODO: Tell user.
            print("---LOGIN ATTEMPT FAILED ---")
            form = AuthenticationForm()
            return render(request, 'pages/loginpage.html', {'form': form})
    else:
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, 'pages/loginpage.html', {'form': form})
        else:
            return redirect("logoutpage")

def signuppage(request):
    # This shows the user the sign-up page.
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

def logoutpage(request):
    # This just shows a page with a log-out button.
    # It does not actually log out the user.
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'pages/logoutpage.html')

def logmeout(request):
    # This will log the user out, and redirect to log-in page.
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")