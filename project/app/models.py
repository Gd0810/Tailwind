from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    

# Create your models here.
