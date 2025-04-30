import pytest
from django.urls import reverse
from main.models import ProductCategory, Product

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
