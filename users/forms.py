from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserData

import openai


def validate_api_key(self, api_key):
    if api_key is not None:
        openai.api_key = api_key
        try:
            openai.Model.list()
        except openai.error.AuthenticationError:
            self.add_error('api_key', 'Invalid api key')
    else:
        self.add_error('api_key', 'Invalid api key')


class UserRegisterForm(UserCreationForm):
    api_key = forms.CharField(
        help_text='Your ChatGPT API key.',
        max_length=51,
        min_length=51,
        required=True,
        label='ChatGPT API key'
    )

    def clean(self):
        cleaned_data = super().clean()
        api_key = cleaned_data.get('api_key')
        validate_api_key(self, api_key)

    class Meta:
        model = User
        fields = ['username', 'api_key', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    api_key = forms.CharField(
        help_text='Your ChatGPT API key.',
        max_length=51,
        min_length=51,
        required=True,
        label='ChatGPT API key'
    )

    def clean(self):
        cleaned_data = super().clean()
        api_key = cleaned_data.get('api_key')
        validate_api_key(self, api_key)

    class Meta:
        model = UserData
        fields = ['api_key']
