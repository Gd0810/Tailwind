from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,subproducts,MyModel

# Create your views here.

def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    return render(request , "products.html" , {"products": products})

def subproduts(request , id):
    product  = Product.objects.get(id=id)
    subproducts = product.subproducts.all()
    return render (request, "subproducts.html", {"product": product, "subproducts": subproducts})


def show_json_data(request):
    # Fetch all instances of MyModel
    objects = MyModel.objects.all()
    return render(request, 'show_json.html', {'objects': objects})





# def products(requset):
#     # products = Product.objects.all()
#     # print(products)
#     # return render(requset , "products.html" , {"prodcuts": products})