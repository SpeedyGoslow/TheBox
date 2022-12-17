from rest_framework import serializers

from .models import products

class productsSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ("id","name","Category","Quantity","Supplier",)
        model = products