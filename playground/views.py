from django.shortcuts import render

from playground.agent import create_agent, query_agent
from playground.forms import FileDataForm
from playground.models import Message, FileData
from playground.utils import decode_response, write_response


def handle_query(request, query):
    # Fetch the file from object
    csv_file = request.user.filedata.file.file
    # Process it and spawn a pd agent
    agent = create_agent(csv_file, request.user.profile.api_key)
    # Create a user message
    user_message = Message.objects.create(
        user=request.user,
        sender=request.user.id,
        content=query,
    )
    # Fetch a response from openAI
    response = query_agent(agent=agent, query=query)
    # Create a openAI message
    res = decode_response(response)
    response_message = Message.objects.create(
        user=request.user,
        sender='open_ai',
        content=write_response(res)
    )
    # Save messages
    user_message.save()
    response_message.save()


def home(request):
    # Fetch FileData object from db
    form = FileDataForm()
    messages = []
    if request.user.is_authenticated:
        file_data = FileData.objects.filter(user=request.user).first()
        if request.method == 'POST':
            if file_data is None:
                form = FileDataForm(request.POST, request.FILES)
                if form.is_valid():
                    file_data = FileData.objects.create(
                        user=request.user,
                        file=form.cleaned_data.get('file'),
                        input=form.cleaned_data.get('input') or "Give me an initial description of the data"
                    )
                    file_data.save()
                    query = file_data.input
                    handle_query(request, query)
            else:
                form = FileDataForm(request.POST, {"file": file_data.file}, instance=file_data)
                if form.is_valid():
                    file_data.save()
                    query = form.cleaned_data.get('input') or "Give me an initial description of the data"
                    handle_query(request, query)
        else:
            if file_data is not None:
                form = FileDataForm(request.GET, {"file": file_data.file}, instance=file_data)
        messages = Message.objects.filter(user=request.user)
    context = {
        'title': 'Home',
        'form': form,
        'responses': messages,
    }
    return render(request, 'home/home.html', context)


def challenge(request):
    context = {
        'title': 'Challenge',
    }
    return render(request, 'challenge/challenge.html', context)
