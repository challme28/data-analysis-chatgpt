from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=35, help_text='Your ChatGPT API key.')

    def __str__(self):
        return f'{self.user.username} Profile'
