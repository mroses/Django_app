#from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
'''
def index(request):
    context = {
        "name":"Indy",
        "students": ["mrose", "tlee"]
    }
    return render(request, 'blogs_app/index.html', context)
'''

def index(request):
    response = "placeholder to later display the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect(index)

def show(request, number):
    response = "placeholder to display blog " + str(number)
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)

def delete(request, number):
    response = "placeholder to delete blog " + str(number)
    return HttpResponse(response)