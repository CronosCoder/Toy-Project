from accounting.models import Transaction
from shop.services import OrderService
from accounting.services.stripe_accounting_service import StripeAccountingService

class TransactionService:
    model_class = Transaction
    order_service = OrderService()
    stripe_accounting_service = StripeAccountingService()

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
        transaction =self.create(**transaction_data)
        stripe_url = self.stripe_accounting_service.create_checkout_session(transaction)
        return stripe_url

    def get_transactions_by_user(self, user):
        return self.model_class.objects.filter(user=user).order_by('-created_at')