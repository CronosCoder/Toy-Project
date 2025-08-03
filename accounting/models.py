from django.db import models
from django.conf import settings
from accounting.constants import TransactionStatus


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='usd')
    status = models.CharField(max_length=2, choices=TransactionStatus.choices, default=TransactionStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} by {self.user.email} - {self.status}"

