from django.urls import path, include

from . import views


urlpatterns = [
    path('users/', views.UserApiViews.as_view()),
    path('profile/<int:pk>', views.UserProfileApiViews.as_view()),
    path('seller-profile/<str:org_name>', views.SellerProfileApiViews.as_view()),
    path('sellers',  views.SellerApiViews.as_view()),
]
