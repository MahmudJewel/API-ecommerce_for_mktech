from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializers
from product.models import Product
# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
