import stripe
from django.conf import settings
from accounting.models import Transaction

stripe.api_key = settings.STRIPE_API_KEY

class StripeAccountingService:
        
    def create_checkout_session(self, transaction: Transaction):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': transaction.currency,
                            'unit_amount': int(transaction.unit_price * 100),  # Convert to cents
                            'product_data': {
                                'name': f'Product {transaction.product_id}',
                            },
                        },
                        'quantity': transaction.quantity,
                    },
                ],
                mode='payment',
                success_url=settings.STRIPE_SUCCESS_URL,
                cancel_url=settings.STRIPE_CANCEL_URL
            )
            return checkout_session.url
        except stripe.error.StripeError as e:
            print(f"Stripe error: {e}")
            raise
        except Exception as error:
            print(f"Unexpected error: {error}")
            raise
