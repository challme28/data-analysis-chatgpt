from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('challenge/', views.challenge, name='challenge'),
    path('auth/', views.auth, name='auth'),
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
]
