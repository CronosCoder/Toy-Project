from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from shop.serializers import OrderCreateSerializer, OrderDetailSerializer
from shop.services import OrderService


class OrderListCreateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderCreateSerializer
    service = OrderService()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderDetailSerializer

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            order = self.service.create_order(serializer.validated_data, request)
            return Response({"message": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            orders = self.service.get_orders_by_user(request)
            serializer = self.get_serializer_class()(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)