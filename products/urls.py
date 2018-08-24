from django.urls import path
from products.views import product_list, product_details

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<id>', product_details, name='product_details'),
    ]