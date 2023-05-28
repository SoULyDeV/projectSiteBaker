from django.shortcuts import render
from django.conf import settings

from .cart import Cart
# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return render(request, 'cart/menu_cart.html')