from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name="prodcuts"),
    path('products/<int:id>/', views.subproduts, name="subproducts"),
    path('show-json/', views.show_json_data, name='show_json_data'),

]