from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from .models import MessageBoard

class HomePageView(ListView):
    model = MessageBoard
    template_name = "home.html"


