from rest_framework import status, generics
from rest_framework.response import Response
from .models import Product
from products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication
