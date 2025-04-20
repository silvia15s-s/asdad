import pytest
from django.contrib.auth import get_user_model
from main.models import Product, ProductCategory, Cart

User = get_user_model()

@pytest.mark.django_db
def test_product_creation():
    category = ProductCategory.objects.create(name="Test Category", slug="test-category")
    product = Product.objects.create(
        category=category,
        title="Test Product",
        description="Test Description",
        price=100.00,
        image_url="http://example.com/image.jpg"
    )
    assert product.title == "Test Product"
    assert str(product) == "Test Product"

@pytest.mark.django_db
def test_cart_creation():
    user = User.objects.create_user(username='testuser', password='testpass123')
    cart = Cart.objects.create(user=user)
    assert str(cart) == f"Cart #{cart.id} for testuser"