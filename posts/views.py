from django.shortcuts import render
from .models import Post

def posts(request):
    posts = Post.objects.all()
    return render(request, 'post_singolo.html', {'posts': posts})