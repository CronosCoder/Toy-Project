from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = 'PE', 'Pending'
    CANCELED = 'CA', 'Canceled'
    FAILED = 'FA', 'Failed'
    COMPLETED = 'CO', 'Completed'
