from django.urls import path, include
from .views import ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewset, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]