from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name="homeview"),
    path('about/', aboutView, name="aboutview"),
    path('post/<slug:slug>/', DetailView, name='detail'),
]