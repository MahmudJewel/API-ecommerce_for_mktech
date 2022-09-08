from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewset, UserViewset, OrderViewset, ProductSearch

router = DefaultRouter()
router.register('product', ProductViewset, basename='product')
router.register('auth', UserViewset, basename='auth')
router.register('order', OrderViewset, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', ProductSearch.as_view(), name='search'),
]