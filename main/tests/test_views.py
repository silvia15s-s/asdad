import pytest
from django.urls import reverse
from main.models import ProductCategory, Product
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_catalog_view(client):
    url = reverse('catalog')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_to_cart_view(admin_client):
    category = ProductCategory.objects.create(name="Category", slug="category")
    product = Product.objects.create(
        category=category,
        title="Product",
        description="Description",
        price=10.0,
        image_url="http://example.com/image.jpg"
    )
    url = reverse('add_to_cart', args=[product.id])
    response = admin_client.post(url)
    assert response.status_code == 302  # Redirect after adding to cart

@pytest.mark.django_db
def test_profile_view(admin_client):
    user = User.objects.create_user(username='testuser', password='testpass')
    admin_client.force_login(user)
    url = reverse('profile')
    response = admin_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_product_detail_view(client):
    category = ProductCategory.objects.create(name="Category", slug="category")
    product = Product.objects.create(
        category=category,
        title="Product",
        description="Description",
        price=10.0,
        image_url="http://example.com/image.jpg"
    )
    url = reverse('product_detail', args=[product.id])
    response = client.get(url)
    assert response.status_code == 200
