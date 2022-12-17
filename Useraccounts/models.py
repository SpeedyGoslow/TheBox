from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class SmeCustomUser(AbstractUser):
    SME_Name = models.CharField(max_length=150,null=True)
    SME_Address = models.CharField(max_length=150,null=True)
    SME_Phone = models.CharField(max_length=10,null=True)
