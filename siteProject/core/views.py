from django.shortcuts import render

#import the class Product from app product to redering it in the templates
from product.models import Product, Category
# Create your views here.
def frontPage(request):
    products = Product.objects.all()[0:8]
    return render(request, 'core/frontpage.html', {'products':products})
# create a new view for the shop page, will get all the products from the db and render them
def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'core/shop.html', context)