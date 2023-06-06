from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
]
