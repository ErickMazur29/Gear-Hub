from django.contrib import admin
from products.models import Products, Brand, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'model_name', 'price','description', 'condition','created_at', 'photo', 'category',)
    search_fields = ('title'),

admin.site.register(Brand, BrandAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
