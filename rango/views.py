# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {'categories': category_list}
    
    # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

    #this is reponse being rendered back
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_about = {'boldmessage': "The king of cats"}
    # return HttpResponse("Rango says here is the about page!<br/> <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_about)
# Create your views here.
