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
            url = self.service.create_transaction(serializer.validated_data, request)
            return Response({"payment_url": url}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class PaymentSuccessAPIView(views.APIView):
    def get(self, request):
        # Handle successful payment logic here
        return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)


class PaymentFailAPIView(views.APIView):
    def get(self, request):
        # Handle failed payment logic here
        return Response({"message": "Payment failed"}, status=status.HTTP_400_BAD_REQUEST)
