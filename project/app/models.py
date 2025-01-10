from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50, null=True, blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class subproducts(models.Model):
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="subproducts" ,verbose_name="Main Product")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50, null=True, blank=True)  
    
    def __str__(self):
        return self.name

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    street = models.CharField(max_length=255 , null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    data = models.JSONField(editable=False)  # Hidden in admin but stores JSON

    def save(self, *args, **kwargs):
        # Construct the JSON data dynamically from separate fields
        self.data = {
            "age": self.age,
            "email": self.email,
            "address": {
                "street": self.street,
                "city": self.city,
                "zipcode": self.zipcode
            }
        }
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class Productz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # PostgreSQL-specific JSONField to store a JSON-encoded object
    specifications = models.JSONField(default=dict, blank=True)
    
    # PostgreSQL-specific ArrayField to store a list of strings
    tags = ArrayField(models.CharField(max_length=100), blank=True)
    
    # PostgreSQL-specific ArrayField to store a list of integers
    stock_levels = ArrayField(models.IntegerField(), blank=True)

    def __str__(self):
        return self.name
