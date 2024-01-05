from rest_framework import serializers
from catalog.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'image', 'description', 'price', 'available', 'modifier_groups',
                  'created', 'updated']
