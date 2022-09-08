from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import generics

from .serializers import ProductSerializers, UserSerializers, OrderSerializers
from product.models import Product
from customer.models import Order
# Create your views here.

# product viewset
class ProductViewset(viewsets.ModelViewSet):
	serializer_class = ProductSerializers
	queryset = Product.objects.all()

	def get_permissions(self):
		if self.request.method == 'GET':
			self.permission_classes = [IsAuthenticatedOrReadOnly, ]
		else:
			self.permission_classes = [IsAdminUser, ]
		return super(ProductViewset, self).get_permissions()


# user viewset 
class UserViewset(viewsets.ModelViewSet):
	serializer_class = UserSerializers
	queryset = User.objects.all()

	def get_permissions(self):
		if self.request.method == 'POST':
			self.permission_classes = [AllowAny, ]
		else:
			self.permission_classes = [IsAdminUser, ]
		return super(UserViewset, self).get_permissions()

# order viewset 
class OrderViewset(viewsets.ModelViewSet):
	serializer_class = OrderSerializers
	queryset = Order.objects.all()

	def get_permissions(self):
		if self.request.method == 'POST':
			self.permission_classes = [IsAuthenticated, ]
		else:
			self.permission_classes = [IsAdminUser, ]
		return super(OrderViewset, self).get_permissions()

# users indivisual order list 
class OrderListView(generics.ListAPIView):
	serializer_class = OrderSerializers
	permission_classes = [IsAuthenticated, ]

	def get_queryset(self):
		user = self.request.user
		return Order.objects.filter(customer=user)


# product search view
class ProductSearch(generics.ListAPIView):
	serializer_class = ProductSerializers

	def get_queryset(self):
		search = self.request.query_params.get('search', None)
		products = Product.objects.all()
		if search is not None:
			products = products.filter(name__contains=search)
		# print(f"Name = {search} and product=> {products}")
		return products