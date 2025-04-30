import unittest
from django.test import TestCase
from django.contrib.auth import get_user_model
from main.models import Product, ProductCategory

User = get_user_model()

class UserProfileModelTests(TestCase):
    def test_userprofile_creation(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        self.assertEqual(user.username, "testuser")

class ProductModelTests(TestCase):
    def test_product_creation(self):
        category = ProductCategory.objects.create(name="Test Category", slug="test-category")
        product = Product.objects.create(
            category=category,
            title="Test Product",
            description="Test Description",
            price=99.99,
            image_url="http://example.com/image.jpg"
        )
        self.assertEqual(product.title, "Test Product")
