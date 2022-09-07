from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import ProductSerializers, UserSerializers
from product.models import Product
# Create your views here.

# product viewset
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

# user viewset 
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
