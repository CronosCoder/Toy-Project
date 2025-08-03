from shop.models import Product, Order

class ProductService:
    model_class = Product

    def get_product_by_id(self, product_id):
        try:
            return self.model_class.objects.get(id=product_id)
        except Exception as e:
            raise Exception(f"Product not found {str(e)}")

    def all(self, **kwargs):
        return self.model_class.objects.filter(**kwargs)

    def create_product(self, data):
        return self.model_class.objects.create(**data)


class OrderService:
    model_class = Order
    product_service = ProductService()

    def create_order(self, validated_data, request):
        product= validated_data.get('product')
        quantity = validated_data.get('quantity', 1)
        if quantity > product.stock:
            raise Exception("Insufficient stock")
        order_data = {
            "user": request.user,
            "product": product,
            "unit_price": product.price,
            "quantity": validated_data.get('quantity', 1),
            "total_amount": product.price * validated_data.get('quantity', 1),
        }
        order =self.model_class.objects.create(**order_data)
        if order:
            product.stock -= order.quantity
            product.save()
        return order

    def get_orders_by_user(self, request):
        if request.user.is_anonymous:
            raise Exception("User is not authenticated")
        user = request.user
        return self.model_class.objects.filter(user=user).order_by('-created_at')

    def update_order_status(self, order, status):
        order.status = status
        order.save()
        return order