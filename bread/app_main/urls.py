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

    # 공지사항
    path('announcement', views.announcement),
    path('announcement_detail', views.announcement_detail),

    # 1:1문의
    path('inquiry', views.inquiry),
    path('inquiry_detail', views.inquiry_detail),

    # 마이페이지
    path('mypage', views.mypage),
    path('mypage_order', views.mypage_order),
    path('mypage_delivery', views.mypage_delivery),
]
