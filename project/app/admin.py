from django.contrib import admin
from .models import Product, subproducts,MyModel,Productz

# Register your models here.

register = admin.site.register(Product)
register = admin.site.register(subproducts)
register = admin.site.register(MyModel)
register = admin.site.register(Productz)


