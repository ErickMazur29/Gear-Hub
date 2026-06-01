from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from products.models import Products
from products.forms import NewProductForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

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
        brand = self.request.GET.get('brand')

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

        if brand:
            queryset = queryset.filter(
                brand__name__icontains=brand # FK, so brand__name
            )

        return queryset.distinct()
    

@method_decorator(login_required(login_url='login'), name='dispatch')
#criar novo produto / anuncio
class NewProduct(CreateView):
    model = Products
    form_class = NewProductForm
    template_name = 'new_product.html'
    success_url = reverse_lazy('products_list')

    def form_valid(self, form):
        form.instance.seller = self.request.user.profile
        return super().form_valid(form)

class DetailProduct(DetailView):
    model = Products
    template_name = 'detail_product.html'
    context_object_name = 'product'



@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteProduct(UserPassesTestMixin, DeleteView):
    model = Products
    template_name = 'delete_product.html'
    context_object_name = 'delete_product'

    def test_func(self):
        product = self.get_object()
        return self.request.user.profile == product.seller

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.request.user.profile.pk})  



@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateProduct(UserPassesTestMixin, UpdateView):
    model = Products
    form_class = NewProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('products_list') 

    def test_func(self):
        product = self.get_object()
        return self.request.user.profile == product.seller

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.request.user.profile.pk})

