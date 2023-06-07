from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    api_key = forms.CharField(help_text='Your ChatGPT API key.', required=True, label='ChatGPT API key')

    class Meta:
        model = User
        fields = ['username', 'api_key', 'password1', 'password2']