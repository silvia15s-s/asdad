import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from main.models import Product, ProductCategory
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_product_list_api():
    client = APIClient()
    ProductCategory.objects.all().delete()
    Product.objects.all().delete()
    category = ProductCategory.objects.create(name="Category1", slug="category1")
    Product.objects.create(
        category=category,
        title="Product1",
        description="Description1",
        price=10.0,
        image_url="http://example.com/image1.jpg"
    )
    url = reverse('product-list')
    response = client.get(url, HTTP_HOST='localhost')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['title'] == "Product1"

@pytest.mark.django_db
def test_product_create_api():
    client = APIClient()
    ProductCategory.objects.all().delete()
    Product.objects.all().delete()
    User.objects.filter(username='admin').delete()
    user = User.objects.create_user(username='admin', password='pass123', is_staff=True)
    client.force_authenticate(user=user)
    category = ProductCategory.objects.create(name="Category2", slug="category2")
    url = reverse('product-list')
    data = {
        "category": category.id,
        "title": "New Product",
        "description": "New Description",
        "price": "20.00",
        "image_url": "http://example.com/image2.jpg",
        "details": "Details",
        "material": "Material",
        "weight": "1kg",
        "installation": "Easy",
        "compatibility": "Universal",
        "features": "Features",
        "achievements": "Achievements"
    }
    response = client.post(url, data, format='json', HTTP_HOST='localhost')
    assert response.status_code == 201
    assert response.data['title'] == "New Product"

@pytest.mark.django_db
def test_product_category_list_api():
    client = APIClient()
    ProductCategory.objects.all().delete()
    ProductCategory.objects.create(name="Category3", slug="category3")
    url = reverse('category-list')
    response = client.get(url, HTTP_HOST='localhost')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Category3"
