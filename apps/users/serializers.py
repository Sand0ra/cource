from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_seller', 'is_superuser']


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class SellerSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['org_name', 'email', 'first_name', 'last_name',]


class SellerProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['org_name', 'email', 'first_name', 'last_name', 'card_number']
