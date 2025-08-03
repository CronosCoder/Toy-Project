from .models import Transaction
from shop.services import OrderService


class TransactionService:
    model_class = Transaction
    order_service = OrderService()

    def create(self, **kwargs):
        return self.model_class.objects.create(**kwargs)

    def create_transaction(self, validated_data, request):
        user = request.user
        order_id = validated_data.get('order_id')
        order = self.order_service.get_order_by_id(order_id)
        
        transaction_data = {
            "user": user,
            "order": order,
            "product_name": order.product.name,
            "product_id": order.product.id,
            "unit_price": order.unit_price,
            "quantity": order.quantity,
            "total_price": order.total_amount,
        }
        return self.create(**transaction_data)

    def get_transactions_by_user(self, user):
        return self.model_class.objects.filter(user=user).order_by('-created_at')