from rest_framework import generics

from .models import products
from .serializers import productsSerializer

# Create your views here.

class  productList(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer
    
    
class productDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = productsSerializer

