from django.urls import path
from rest_framework import routers

from .views import *
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [

    path('categories', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products', ProductListAPIView.as_view(), name='product-list'),
    path('categories/<int:category_id>/<int:pk>', ProductDetailAPIView.as_view(), name='product-detail'),
    path('register/', registerAPI, name='registration'),
    path('login/', loginAPI, name='log_in'),
    *router.urls,

]
