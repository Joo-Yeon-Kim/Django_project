from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.object.all()
    return request(request, 'home.html',{'blogs' : blogs})