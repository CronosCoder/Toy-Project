from rest_framework import serializers


class TransactionCreateSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
