from django.urls import path

from . import views


urlpatterns = [
    path('add_product', views.AddProductApiViews.as_view()),
    path('products/', views.ProductListApiViews.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductRetrieveUpdateDestroyApiViews.as_view(), name='product'),
    path('category/', views.CategoryListCreateApiViews.as_view(), name='category'),
]
