from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
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

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.brand} {self.model_name}'
    