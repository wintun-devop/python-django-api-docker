from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    quantity = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        fields = ('__all__')