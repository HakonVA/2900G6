from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def loginpage(request):

    # If user is already logged in, redirect to logout page
    if request.user.is_authenticated:
        return redirect("logoutpage")

    # User is trying to log in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Login succesful
        if user is not None:
            login(request, user)
            messages.info(request, "Successfully logged in as {}".format(username))
            return redirect("home")
        
        # Invalid login
        else:
            form = AuthenticationForm()
            messages.error(request, "Login failed.")
            return render(request, 'users/loginpage.html', {'form': form})
    
    # Handle GET request
    else:
        form = AuthenticationForm()
        return render(request, 'users/loginpage.html', {'form': form})

def signuppage(request):
    
    # If user is already logged in, redirect to logout page
    if request.user.is_authenticated:
        return redirect("logoutpage")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.info(request, "Registred and logged in as {}".format(username))
            return redirect('home')
        
        else:
            messages.error(request, "")
            return render(request, 'users/signuppage.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'users/signuppage.html', {'form': form})

def logoutpage(request):
    # This is the "logout" resource
    # This just shows a page with a log-out button.
    # It does not actually log out the user.
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'users/logoutpage.html')

def logmeout(request):
    # This will log the user out, and redirect to log-in page.
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You were logged out.")
    return redirect("login")