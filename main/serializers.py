from rest_framework import serializers
from .models import Product, ProductCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'description', 'price', 'image_url', 'details', 'material', 'weight', 'installation', 'compatibility', 'features', 'achievements']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'slug']
