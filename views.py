from __future__ import unicode_literals

from django.shortcuts import render

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
    #response = "placeholder"
    return HttpResponse(response)