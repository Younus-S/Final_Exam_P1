from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import BlogPost
from .models import Product

# Create your views here.

def blogposts(request):

  posts = BlogPost.objects.all().values()
  template = loader.get_template('blogpost.html')
  context = {
    'posts': posts
  }
  return HttpResponse(template.render(context, request))

def product_list_view(request):

  products = Product.objects.all().values()
  template = loader.get_template('product_list.html')
  context = {
    'products': products
  }
  return HttpResponse(template.render(context, request))
