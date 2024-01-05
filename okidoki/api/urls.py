from django.urls import path
from .views import CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, ProductDetailAPIView

app_name = 'api'

urlpatterns = [
    path('categories', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
]