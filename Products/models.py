from django.db import models
from django.conf import settings

category =(
    ('Perishables','Perishables'),
    ('Electronics','Electronics'),
    ('Stationary','Stationary'),
)


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=150,null=True)
    Category = models.CharField(max_length=70,choices=category,null=True)
    Quantity = models.PositiveBigIntegerField(null=True)
    Supplier = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
   
    class Meta:
        verbose_name_plural = 'Products'
    
    
    def __str__(self):
        return f'{self.name} By supplied by {self.Supplier.SME_Name}' 
  

    
    