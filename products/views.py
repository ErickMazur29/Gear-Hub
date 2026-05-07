from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from products.models import Products
from products.forms import NewProductForm
from django.urls import reverse_lazy

# Create your views here.

#produtos / anuncios
class ProductsList(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')

        if search:
            queryset = queryset.filter(
                title__icontains=search
            ) | queryset.filter(
                model_name__icontains=search
            ) | queryset.filter(
                brand__name__icontains=search  # FK, so brand__name
            )

        if category:    
            queryset = queryset.filter(
                category__name__icontains=category  # FK, so category__name
            )

        return queryset.distinct()
    
#criar novo produto / anuncio
class NewProduct(CreateView):
    model = Products
    form_class = NewProductForm
    template_name = 'new_product.html'
    success_url = reverse_lazy('products_list')

class DetailProduct(DetailView):
    model = Products
    template_name = 'detail_product.html'
    context_object_name = 'product'