from django.shortcuts import render
import requests


url = 'https://newsapi.org/v2/top-headlines'
params = {
        'sources': 'techcrunch',
        'apiKey': 'c4b476f264c8431c9716206176d054a1'
    }

response = requests.get(url, params=params)
data = response.json()
articles = data['articles']


# Create your views here.

def get_date(post):
  return post['publishedAt']

def index(request):
  sorted_posts = sorted(articles, key=get_date)
  latest_posts = sorted_posts[-6:]
  popular_posts = sorted_posts[1:4]
  return render(request, "healthblog/index.html", {"posts": latest_posts,
                                                   "restposts": popular_posts})

