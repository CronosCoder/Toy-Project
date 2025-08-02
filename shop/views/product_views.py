
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from shop.serializers import ProductCreateSerializer, ProductDetailSerializer
from shop.services import ProductService

class ProductListCreateView(views.APIView):
    service = ProductService()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductDetailSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]

    def get(self, request):
        products = self.service.all()
        serializer = self.get_serializer_class()(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            product = self.service.create_product(serializer.validated_data)
            detail_serializer = ProductDetailSerializer(product)
            return Response(detail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
