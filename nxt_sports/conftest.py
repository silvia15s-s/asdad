import pytest
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nxt_sports.settings')
django.setup()

@pytest.fixture
def client():
    from django.test import Client
    return Client()

@pytest.fixture
def admin_client(client):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='testpass123'
    )
    client.force_login(admin)
    return client
