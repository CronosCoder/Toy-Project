
from rest_framework import serializers
from shop.models import Product, Category, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock', 'model_number']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'price', 'stock', 'model_number']

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Order
        fields = ['id', 'product', 'unit_price', 'quantity', 'total_amount', 'status', 'created_at']
