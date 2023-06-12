from django.shortcuts import render, redirect
from django.contrib import messages

from playground.utils import decode_response, write_response
from playground.agent import create_agent, query_agent
from users.models import Profile


def handle_initial_query(request):
    try:
        csv_file = request.FILES["file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect('home')
        if csv_file.multiple_chunks():
            messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
            return redirect('home')

        profile = Profile.objects.get(user=request.user)
        agent = create_agent(csv_file, profile.api_key)
        response = query_agent(agent=agent, query="Give me an initial description of the data")
        return decode_response(response)
    except Exception as e:
        messages.error(request, "Unable to upload file. " + repr(e))


def home(request):
    decoded_response = ''
    if request.method == 'POST':
        decoded_response = handle_initial_query(request)
    context = {
        'title': 'Home',
        'response': write_response(decoded_response),
    }
    return render(request, 'home/home.html', context)


def challenge(request):
    context = {
        'title': 'Challenge',
    }
    return render(request, 'challenge/challenge.html', context)
