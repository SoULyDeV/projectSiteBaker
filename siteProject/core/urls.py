from django.contrib.auth import views
from django.urls import path

from core.views import frontPage, shop, signup
from product.views import product



urlpatterns = [
    path('', frontPage, name='front-page'),
    path('signup', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    path('login', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]
