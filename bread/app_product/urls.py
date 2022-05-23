from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

app_name = "app_product"

urlpatterns = [
    path('', views.product_list), 
    path('category', views.product_category), 
    path('detail', views.product_detail), 
    path('cart', views.cart), 
]
