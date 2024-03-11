from django.shortcuts import render
from .models import Post

def contatti(request):
    return render(request, 'contatti.html')