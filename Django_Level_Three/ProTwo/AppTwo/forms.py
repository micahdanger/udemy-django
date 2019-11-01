from django import forms
from AppTwo.models import Users

class NewUserForm(forms.ModelForm):
    # custom validation will go here
    class Meta():
        model = Users
        fields = '__all__'
