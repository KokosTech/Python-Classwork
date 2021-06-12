from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>This is definitely a post</h1><p>Wow, this is a paragraph</p><ul><li>I only get bullet list</li></ul>')
