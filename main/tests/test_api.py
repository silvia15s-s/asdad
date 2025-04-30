import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from main.models import Product, ProductCategory
from main.models import UserProfile as User

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
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1

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
        "features": "Features",
        "achievements": "Achievements"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201

@pytest.mark.django_db
def test_product_update_delete_api():
    client = APIClient()
    User.objects.filter(username='admin2').delete()
    user = User.objects.create_user(username='admin2', password='pass123', is_staff=True)
    client.force_authenticate(user=user)
    category = ProductCategory.objects.create(name="CategoryUpdate", slug="categoryupdate")
    product = Product.objects.create(
        category=category,
        title="Old Product",
        description="Old Description",
        price=30.0,
        image_url="http://example.com/image.jpg",
        features="Features",
        achievements="Achievements"
    )
    url = reverse('product-detail', args=[product.id])
    data_update = {
        "title": "Updated Product",
        "description": "Updated Description",
        "price": "35.00",
        "image_url": "http://example.com/image_updated.jpg",
        "features": "Features",
        "achievements": "Achievements"
    }
    response = client.put(url, data_update, format='json')
    assert response.status_code == 200

    response_delete = client.delete(url)
    assert response_delete.status_code == 204
