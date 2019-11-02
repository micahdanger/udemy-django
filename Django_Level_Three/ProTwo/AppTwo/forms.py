from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    # custom validation will go here

    # Meta() indicates that we need to include all parts of the user model in the form
    class Meta():
        model = User
        fields = '__all__'
