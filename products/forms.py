from django import forms
from products.models import Products

class NewProductForm (forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title','brand','model_name','price','description','condition','photo','category']

        