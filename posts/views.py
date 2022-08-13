from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Post

class HomePageView(TemplateView):
    model = Post
    template = 'home.html'
    