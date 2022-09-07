from rest_framework import serializers

from product.models import Product

# product serializers 
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'