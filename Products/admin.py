from django.contrib import admin
from .models import products
# Register your models here.

admin.site.site_header ='The Box'

admin.site.register(products)