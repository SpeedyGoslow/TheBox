from django.views.generic import ListView
from .models import products


# Create your views here.

class ProductListView(ListView):
    model = products
    template_name = 'Products/Productlist.html'

