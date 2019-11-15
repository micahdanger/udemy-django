from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

# THIS DECORATOR HANDLES THE REQUIREMENT FOR USERS TO BE LOGGED IN
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")

def register(request):

    context_dict = {}

    registered = False

    if request.method == "POST":
        # here's where the data comes back from the page and we start working with it
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # here's the One-To-One relation we put into the model
            profile.user = user

            # if a profile pic is in the POST, save that shit
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        # if either form is invalid, print the errors
        else:
            print(user_form.errors, profile_form.errors)
    # if the http request wasn't a POST
    else:
        # instantiate a new user
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # fill up the dict with all the treats needed in the registration.html
    context_dict['registered'] = registered
    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form

    return render(request, 'basic_app/registration.html', context_dict)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # THIS REDIRECTS THE USER BACK TO THE HOMEPAGE
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active.")

        else:
            print("Someone tried to login and failed.")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request, 'basic_app/login.html', {})
