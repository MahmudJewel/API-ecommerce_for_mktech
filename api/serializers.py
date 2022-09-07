from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from product.models import Product

# product serializers


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# user serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name']  # '__all__'

    def create(self, validated_data):
        new_user = User(**validated_data)

        new_user.password = make_password(validated_data.get('password'))

        new_user.save()

        return new_user
