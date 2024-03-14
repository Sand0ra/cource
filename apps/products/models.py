from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Category', max_length=100)
    photo = models.ImageField('Photo', upload_to='category/')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('Product', max_length=100)
    price = models.IntegerField('Price')
    photo = models.ImageField('Photo', upload_to='product/')
    description = models.TextField('Description', blank=True, null=True)
    expiration_date = models.DateField('expiration date', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ProductCategory')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_product')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
