from django.shortcuts import render

from .models import Post
# Create your views here.

def index(request):
    context = dict()
    posts = Post.objects.filter(is_public=True).all()
    context['posts'] = posts
    return render(request, 'index.html', context)


def about(request):
    context = dict()
    return render(request, 'about.html', context)


def contact(request):
    context = dict()
    return render(request, 'contact.html', context)


def post(request):
    context = dict()
    return render(request, 'post.html', context)
