from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

#import views from our app 'core'




urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
