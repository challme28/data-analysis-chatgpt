from django.shortcuts import render


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home/home.html', context)


def challenge(request):
    context = {
        'title': 'Challenge',
    }
    return render(request, 'challenge/challenge.html', context)


def auth(request):
    context = {
        'title': 'Auth',
    }
    return render(request, 'auth/auth.html', context)


def upload(request):
    return render(request, 'upload/upload.html')


def result(request):
    return render(request, 'result/result.html')
