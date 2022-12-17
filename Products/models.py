from django.db import models

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
    
      
    class Meta:
        verbose_name_plural = 'Products'
    
    
    def __str__(self):
        return self.name
  

    
    