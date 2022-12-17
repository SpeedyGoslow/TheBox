from django.urls import path
from .views import productList,productDetail

urlpatterns= [
    path("<int:pk>/",productDetail.as_view(),name="product_Details"),
    path("",productList.as_view(),name="product_List"),
]