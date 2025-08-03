from django.db import models


class TransactionStatus(models.TextChoices):
    PENDING = 'PE', 'Pending'
    CONFIRMED = 'CO', 'Confirmed'
    FAILED = 'FA', 'Failed'