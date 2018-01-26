# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    # this queries Category model to retrieve top five cate
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

    #this is reponse being rendered back
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_about = {'boldmessage': "The king of cats"}
    # return HttpResponse("Rango says here is the about page!<br/> <a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_about)

def show_category(request, category_name_slug):
    #create a context dictionary which we can pass to template rendering engine
    context_dict={}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        #Retrieve all of the assosicated pages.
        #Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        #adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary
        # well use this in the template to verify that the categories exists
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didnt find the specified category.
        # Dont do anything
        # the templates will display the "no category' message
        context_dict['category'] = None
        context_dict['pages'] = None

        # Go render the response and return it to the client
        return render(request, 'rango/category.html', context_dict)

