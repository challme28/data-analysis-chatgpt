from django.shortcuts import render


def auth(request):
    context = {
        'title': 'Auth',
    }
    return render(request, 'auth/auth.html', context)


def upload(request):
    return render(request, 'upload/upload.html')


def result(request):
    return render(request, 'result/result.html')
