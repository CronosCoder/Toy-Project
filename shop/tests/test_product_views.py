from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from core.models import User
from shop.models import Product, Category

class ProductListCreateViewTest(APITestCase):
    def setUp(self):
        self.list_url = reverse('product_list_create')
        self.admin_user = User.objects.create_superuser(email='super@admin.com', password='adminpass123')
        self.category = Category.objects.create(name='Test Category')
        self.product_data = {
            'category': self.category.id,
            'name': 'Test Product',
            'price': 10.99,
            'description': 'This is a test product.',
            'stock': 100,
            'model_number': 'TP-001'
        }
        Product.objects.create(name='Existing Product', price=5.99, category=self.category, description='Existing', stock=10, model_number='EX-001')

    def test_get_products_public(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_post_product_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(self.list_url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.product_data['name'])

    def test_post_product_as_non_admin(self):
        user = User.objects.create_user(email='user@example.com', password='userpass')
        self.client.force_authenticate(user=user)
        response = self.client.post(self.list_url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_product_unauthenticated(self):
        response = self.client.post(self.list_url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
