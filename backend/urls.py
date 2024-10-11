
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from orders.views import OrderViewSet
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [             
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),  # For login/logout
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



