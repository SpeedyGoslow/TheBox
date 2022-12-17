from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import products

class productsSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ("id","name","Category","Quantity","Supplier",)
        model = products
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ("id","username")