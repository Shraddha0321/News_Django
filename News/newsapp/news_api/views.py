from django.shortcuts import render
import requests
API_KEY ='a249d9991c4c469b8e82e51e0c2e88d0'
# Create your views here.
def home(request):
    url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}'
    response = request.get(url)
    data = response.json()

    articles = data['articles']

    context ={
        'articles': articles
    }

    return render (request, 'news_api/home.html', context)