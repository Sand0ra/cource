from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = CustomUserManager()
    username = None
    email = models.EmailField(
        verbose_name='Почта',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_seller = models.BooleanField(default=False)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True, unique=True)

    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email


