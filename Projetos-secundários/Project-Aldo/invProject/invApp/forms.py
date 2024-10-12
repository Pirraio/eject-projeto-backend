from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        label = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_ID': forms.NumberInput(attrs={'placeholder':'ex: 1','class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'ex: shirt','class':'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder':'ex: S12345','class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'ex: 19.99','class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'ex: 10','class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'ex: ABC corp','class':'form-control'}),
        }