from django.urls import path
from . import views as post_view
from django.views.generic import ListView, DeleteView
from .models import Post

urlpatterns = [
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = 'lista_post.html',
        paginate_by = 5), name='lista'),
        
    
    path('<int:id>/<slug:slug>/', DeleteView.as_view(
        model = Post,
        template_name = 'post_singolo.html',), name='singolo'),
    path('', post_view.contatti, name='contatti'),
]