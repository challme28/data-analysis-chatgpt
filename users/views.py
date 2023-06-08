from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import UserData


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            api_key = form.cleaned_data.get('api_key')
            messages.success(request, f'Your account has been created.')
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(user=user, api_key=api_key)
            user_data.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    user = UserData.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)
