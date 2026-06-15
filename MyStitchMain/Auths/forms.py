from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import AppUser


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['phone', 'gender']

class LoginForm(AuthenticationForm):
    pass  