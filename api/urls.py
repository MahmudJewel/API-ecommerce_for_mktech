from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewset, UserViewset, OrderViewset, ProductSearch, OrderListView

router = DefaultRouter()
router.register('product', ProductViewset, basename='product')
router.register('auth', UserViewset, basename='auth')
router.register('order', OrderViewset, basename='order')

urlpatterns = [
    # router 
    path('', include(router.urls)),

    # indivisual order list
    path('authorder/', OrderListView.as_view(), name='authorder'),

    # Search product
    path('search/', ProductSearch.as_view(), name='search'),
]