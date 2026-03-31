from django.test import TestCase
from store.models import Product, ProductCategory

class ProductCategoryTest(TestCase):
    def setUp(self):
        self.cat = ProductCategory.objects.create(name='Books', description='Security books')

    def test_category_str(self):
        self.assertEqual(str(self.cat), 'Books')

class ProductTest(TestCase):
    def setUp(self):
        self.cat = ProductCategory.objects.create(name='Tools')
        self.product = Product.objects.create(
            name='Scanner',
            slug='scanner',
            description='Port scanner',
            price=99.99,
            category=self.cat,
            stock=10,
            available=True
        )

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Scanner')