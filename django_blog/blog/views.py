from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Post 1',
        'date_posted': 'Feb 5, 2024',
        'content': "Content of Post1"
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'date_posted': 'Feb 5, 2024',
        'content': "Content of Post2"
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context)