from django.urls import path
from .views import UserViewset, ProductViewset
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users',UserViewset,basename="users")
router.register('',ProductViewset,basename="Products")

urlpatterns= router.urls