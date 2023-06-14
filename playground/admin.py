from django.contrib import admin
from .models import Message, FileData

admin.site.register([Message, FileData])
