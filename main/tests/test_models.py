import pytest
from main.models import UserProfile as User, Product, ProductCategory, Cart, CartItem
from decimal import Decimal

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

@pytest.mark.django_db
def test_userprofile_fields():
    User.objects.filter(username='profileuser').delete()
    user = User.objects.create_user(username='profileuser', password='pass123')
    profile = UserProfile.objects.get(username='profileuser')
    profile.phone = "1234567890"
    profile.address = "Test Address"
    profile.card_number = "1111222233334444"
    profile.save()
    assert profile.phone == "1234567890"
    assert profile.address == "Test Address"
    assert profile.card_number == "1111222233334444"

@pytest.mark.django_db
def test_userprofile_get_absolute_url():
    User.objects.filter(username='urluser').delete()
    user = User.objects.create_user(username='urluser', password='pass123')
    profile = UserProfile.objects.get(username='urluser')
    url = profile.get_absolute_url()
    assert url == "/profile/"
