from multiprocessing import context
from django.shortcuts import render

def product_list(request):
    context = {
        'banner_title':'제품소개'
    }
    return render(request, 'product_list.html', context=context)

def product_category(request):
    context = {
        'banner_title':'제품소개'
    }
    return render(request, 'product_category.html', context=context)

def product_detail(request):
    context = {
        'banner_title':'제품소개'
    }
    return render(request, 'product_detail.html', context=context)

def cart(request):
    context = {
        'banner_title':'장바구니'
    }
    return render(request, 'cart.html', context=context)