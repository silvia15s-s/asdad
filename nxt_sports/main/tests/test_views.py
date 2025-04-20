import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_catalog_view(client):
    response = client.get(reverse('catalog'))
    assert response.status_code == 200
    assert 'CATALOG' in str(response.content)

@pytest.mark.django_db
def test_add_to_cart_view(admin_client):
    from main.models import Product, ProductCategory
    category = ProductCategory.objects.create(name="Test", slug="test")
    product = Product.objects.create(
        category=category,
        title="Test Product",
        description="Test",
        price=100,
        image_url="http://example.com/image.jpg"
    )
    
    response = admin_client.get(reverse('add_to_cart', args=[product.id]))
    assert response.status_code == 302