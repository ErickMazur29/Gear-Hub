from django import forms
from products.models import Products

class NewProductForm (forms.ModelForm):

    new_brand = forms.CharField(
        max_length=100,
        required=False
    )
    class Meta:
        model = Products
        fields = ['title','brand', 'new_brand','model_name','price','description','condition','photo','category']


        