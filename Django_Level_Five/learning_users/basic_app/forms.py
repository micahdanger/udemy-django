from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    """
    this inherits from the User class made available through Django
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    """
    this inherits from the model made in models.py
    """
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
