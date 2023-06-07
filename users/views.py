from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .models import UserData


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            api_key = form.cleaned_data.get('api_key')
            messages.success(request, f'Account created for {username}')
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(user=user, api_key=api_key)
            user_data.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
