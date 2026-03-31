from django.test import TestCase
from store.forms import ProductForm, OrderForm
from store.models import ProductCategory

class ProductFormTest(TestCase):
    def setUp(self):
        self.cat = ProductCategory.objects.create(name='Tools')

    def test_valid_product_form(self):
        data = {
            'name': 'New Tool',
            'slug': 'new-tool',
            'description': 'Desc',
            'price': 49.99,
            'category': self.cat.id,
            'stock': 5,
            'available': True,
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    def test_price_negative_fails(self):
        data = {
            'name': 'Bad',
            'slug': 'bad',
            'description': 'Desc',
            'price': -10,
            'category': self.cat.id,
            'stock': 5,
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)