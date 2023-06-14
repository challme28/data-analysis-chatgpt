from django.contrib.auth.models import User
from django.db import models


class FileData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(default='default.csv', upload_to='csv_files')
    input = models.TextField()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
