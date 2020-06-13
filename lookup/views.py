from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    import json
    import requests

    api_request = requests.get(
        "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10006&distance=25&API_KEY=ACBFBC5C-3235-4E72-9E00-5B58BA6344D8")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error'

    context={'api': api}
    return render(request, 'index.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)
