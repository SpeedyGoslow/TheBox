from rest_framework import generics, permissions
from .models import products
from .serializers import productsSerializer
from .permissions import IsSupplierOrReadOnly

# Create your views here.

class  productList(generics.ListCreateAPIView):
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = products.objects.all()
    serializer_class = productsSerializer
    
    
class productDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =  (IsSupplierOrReadOnly,)
    queryset = products.objects.all()
    serializer_class = productsSerializer

