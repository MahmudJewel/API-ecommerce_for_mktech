from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewset, UserViewset

router = DefaultRouter()
router.register('product', ProductViewset, basename='product')
router.register('auth', UserViewset, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]