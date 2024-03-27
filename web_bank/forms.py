from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from web_bank.models import Client


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Login',
        widget=forms.TextInput()
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Password repeat',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(LoginView):
    username = forms.CharField(
        label='Login',
        widget=forms.TextInput()
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password1']
