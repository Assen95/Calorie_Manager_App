from django.shortcuts import render
import requests
import json


def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'wP0qjZRvN+TgOsDjBQm7BQ==kax9fC3z7V4ZIPia'})

        try:
            api = json.loads(api_request.content)
            print(api_request.content)
            if api == []:
                raise ValueError
        except ValueError as e:
            api = "oops! There was an error"
            print(e)
        print(api)
        return render(request, 'home.html', {'api': api})
    else:
        context = {
            'query': "Enter a valid query!",
        }
        return render(request, 'home.html', context)
