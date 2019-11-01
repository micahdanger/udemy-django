from django.shortcuts import render
# ADDED THIS
from django.http import HttpResponse
# Create your views here.
from AppTwo.forms import NewUserForm

def index(request):
    return HttpResponse('<em>My Second App</em>')


def help(request):
    help_dict = {"help_tag": "Help Page"}
    return render(request, "AppTwo/help.html", context=help_dict)


def users(request):

    form = NewUserForm()

    if request.method == "Post":
        form = NewUserForm(request.POST)

        # it the form is valid, we'll put it in the db and save
        if form.is_valid():
            form.save(commit=True)

            # this will take the user back to the home page
            return index(request)
        else:
            print('ERROR, FORM INVALID')

    return render(request, 'AppTwo/users.html', {'form': form})
