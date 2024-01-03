from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import *

# Create your views here.

class HomeView(ListView):
    model = HomePostNews
    fileds = '__all__'
    template_name = 'index.html'
    context_object_name = "home_yangiliklar"




def DetailView(request, slug):
    post = HomePostNews.objects.filter(slug=slug)
    content = {
        "post": post
    }
    return render(request, 'detail.html', content)


def aboutView(request):
    about_me = AboutMe.objects.all()
    content = {
        "about_me": about_me
    }
    return render(request, 'about.html', content)
