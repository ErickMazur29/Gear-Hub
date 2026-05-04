from django.shortcuts import render
from django.views.generic import ListView
from products.models import Products

# Create your views here.

class Products(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'products'