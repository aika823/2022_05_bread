from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

app_name = "app_main"

urlpatterns = [
    path('', views.index), 
    path('signup', views.signup),
    path('signin', views.signin),
    path('find_info', views.find_info),
]
