from django.contrib import admin
from products.models import Products, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'model_name', 'price','description', 'condition','created_at', 'photo')
    search_fields = ('title'),

admin.site.register(Brand, BrandAdmin)
admin.site.register(Products, ProductsAdmin)
# Register your models here.
