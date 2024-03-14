from django.contrib.auth import get_user_model

from rest_framework import generics

from .serializers import UserSerializer, UserProfileSerializer,  SellerProfileSerializer, SellerSerializer

User = get_user_model()


class UserApiViews(generics.ListCreateAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_seller=False)


class UserProfileApiViews(generics.RetrieveUpdateAPIView):

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.filter(is_seller=False)


class SellerApiViews(generics.ListCreateAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        return User.objects.filter(is_seller=True)

    def perform_create(self, serializer):
        serializer.save(is_seller=True)


class SellerProfileApiViews(generics.RetrieveUpdateAPIView):
    serializer_class = SellerProfileSerializer
    lookup_field = "org_name"

    def get_queryset(self):
        return User.objects.filter(is_seller=True)
