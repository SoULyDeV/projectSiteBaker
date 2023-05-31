from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

from .cart import Cart
# Create your views here.

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return render(request, 'cart/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

#login_required = decorato let u geting in only if u are registered
@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')