from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounting.serializers import TransactionCreateSerializer
from accounting.services import TransactionService


class TransactionCreateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    service = TransactionService()
    serializer_class = TransactionCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            transaction = self.service.create_transaction(serializer.validated_data, request)
            return Response({"message": "Transaction created successfully", "transaction_id": transaction.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
