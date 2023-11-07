from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):

    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'wP0qjZRvN+TgOsDjBQm7BQ==kax9fC3z7V4ZIPia'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return render(request, 'home.html')
