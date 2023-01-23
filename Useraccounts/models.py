from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ManufacturerCustomUser(AbstractUser):
    Manufacturer_Name = models.CharField(max_length=150,null=True)
    Manufacturer_Address = models.CharField(max_length=150,null=True)
    Manufacturer_Phone = models.CharField(max_length=10,null=True)
