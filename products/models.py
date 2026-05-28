from django.db import models
from accounts.models import Profile


#Categoria dos Produtos
class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


#Marca dos produtos
class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    

#Produtos a venda    
class Products(models.Model):
    CONDICIONAL_CHOICES = [
        ('New', 'Novo'),
        ('Used', 'Usado'),
    ]

    #criar categoria e vendedor (category & seller)
    title = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product_brand')
    model_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    condition = models.CharField(max_length=5, choices=CONDICIONAL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category', null=True)
    seller = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='product_seller', null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.brand} {self.model_name}'
    