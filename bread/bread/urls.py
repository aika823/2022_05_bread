from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # Django Admin
    path('admin/', admin.site.urls),
    
    # Django Allauth
    path('accounts/', include('allauth.urls')),
    
    # Custom Apps
    path("", include("app_main.urls")),
    path("product/", include("app_product.urls")),
    path("api/", include("app_api.urls")),
    path("manage/", include("app_manage.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)