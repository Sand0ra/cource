from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

from .permissions import IsOwnerOrReadOnly, IsSeller
from rest_framework.permissions import IsAuthenticated


class AddProductApiViews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]


class ProductListApiViews(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyApiViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class CategoryListCreateApiViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
