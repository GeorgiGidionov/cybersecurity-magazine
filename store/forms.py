from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['created_at', 'updated_at']  # изключени полета
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Detailed product description...'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'name': 'Product Name',
            'slug': 'URL Slug',
            'price': 'Price (USD)',
            'stock': 'Quantity in Stock',
            'available': 'Available for purchase?',
        }
        help_texts = {
            'slug': 'Used in the product URL. Must be unique.',
            'stock': 'Enter 0 if out of stock.',
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'customer_name', 'customer_email', 'customer_phone']
        widgets = {
            'customer_phone': forms.TextInput(attrs={'placeholder': 'Optional'}),
        }
        labels = {
            'product': 'Select Product',
            'quantity': 'Quantity',
            'customer_name': 'Your Full Name',
            'customer_email': 'Email Address',
            'customer_phone': 'Phone Number',
        }
        error_messages = {
            'customer_email': {
                'required': 'Email is required to confirm your order.',
                'invalid': 'Enter a valid email address.',
            },
        }

    def clean_quantity(self):
        qty = self.cleaned_data.get('quantity')
        if qty < 1:
            raise forms.ValidationError('Quantity must be at least 1.')
        return qty