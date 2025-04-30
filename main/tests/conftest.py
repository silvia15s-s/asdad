import os
import django

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nxt_sports.settings')
    django.setup()
