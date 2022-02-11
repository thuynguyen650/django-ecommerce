from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('name','email','phone',)