import pytest
from django.contrib.auth import get_user_model
from main.models import Product, ProductCategory, Cart, UserProfile, CartItem
from decimal import Decimal

User = get_user_model()

@pytest.mark.django_db
def test_product_creation():
    ProductCategory.objects.filter(slug="test-category").delete()
    category = ProductCategory.objects.create(name="Test Category", slug="test-category")
    product = Product.objects.create(
        category=category,
        title="Test Product",
        description="Test Description",
        price=Decimal('100.00'),
        image_url="http://example.com/image.jpg"
    )
    assert product.title == "Test Product"
    assert str(product) == "Test Product"

@pytest.mark.django_db
def test_cart_creation():
    User.objects.filter(username='testuser').delete()
    ProductCategory.objects.filter(slug="test-category").delete()
    user = User.objects.create_user(username='testuser', password='testpass123')
    profile = UserProfile.objects.get(username='testuser')
    category = ProductCategory.objects.create(name="Test Category", slug="test-category")
    cart = Cart.objects.create(user=profile)
    product = Product.objects.create(
        category=category,
        title="Test Product",
        description="Test Description",
        price=Decimal('99.99'),
        image_url="http://example.com/image.jpg"
    )
    cart_item = CartItem.objects.create(cart=cart, product=product, quantity=2)
    assert cart.total_price == Decimal('199.98')
    assert cart.total_items == 1
    assert cart_item.total_price == Decimal('199.98')
    assert str(cart) == f"Cart #{cart.id} for testuser"
