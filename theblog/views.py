from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . models import Post
from . forms import PostForm
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class Articalview(DetailView):
    model = Post
    template_name = 'details.html'

class Addpostview(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'