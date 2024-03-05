from rest_framework import serializers
from catalog.models import Category, Product
from orders.models import Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'image', 'description', 'price', 'available', 'modifier_groups',
                  ]


# Сериализатор для модели Order
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'name', 'phone_number', 'entrance', 'address', 'floor', 'flat',
                  'comment', 'delivery', 'pal', 'created', 'paid', 'confirmed', 'cancelled',
                  'production_time', 'items']

    name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    entrance = serializers.IntegerField(required=False)
    address = serializers.CharField(required=False)
    floor = serializers.IntegerField(required=False)
    flat = serializers.IntegerField(required=False)
    comment = serializers.CharField(required=False)
    delivery = serializers.CharField(required=False)
    pal = serializers.CharField(required=False)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
