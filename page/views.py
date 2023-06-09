from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post


class HomePageView(ListView):
    model = Post
    context_object_name = 'all_post_list'
    template_name = 'home.html' 

class DetailPostPage(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class AboutPageView(TemplateView):
    template_name = 'about.html'
