from django.db.models import Q
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
    
#create a way to get the active category
    active_category = request.GET.get('category', '')
#we can filter by category__slug and get only the products with the slug in the url   
    if active_category:
        products = products.filter(category__slug=active_category)
#and then we can render the products they are in the active category


#here we want to get the products we are searching for in the search  
    query = request.GET.get('query', '')
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))    
# and then we can render the products they are, by the name or description with __icontains!   
    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }
    return render(request, 'core/shop.html', context)