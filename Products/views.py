from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import products
from .serializers import productsSerializer, UserSerializer
from .permissions import IsSupplierOrReadOnly


# Create your views here.

class  ProductViewset(viewsets.ModelViewSet):
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = products.objects.all()
    serializer_class = productsSerializer
     
class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()

    serializer_class = UserSerializer
    
 
    
    


