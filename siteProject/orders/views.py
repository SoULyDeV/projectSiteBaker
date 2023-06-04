from django.shortcuts import render, redirect

from cart.cart import Cart

# Create your views here.
from .models import Order, OrderItem

def start_order(request):
    
    cart = Cart(request)
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        
        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, address=address,  zipcode=zipcode, place=place, email=email, phone=phone)
        
        for item in cart:
            product = item['product']
            quantity = int(item['quantity']) 
            price = product.price * quantity
            
            item = OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            
            
        return redirect('myaccount')
        cart.clear()
    
    return redirect('cart')