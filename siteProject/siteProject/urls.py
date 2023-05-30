
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

#import views from our app 'core'
from cart.views import add_to_cart, cart, checkout
from core.views import frontPage, shop, signup
from product.views import product

urlpatterns = [
    path('', frontPage, name='front-page'),
    path('signup', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    path('login', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('cart/checkout', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),        
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
