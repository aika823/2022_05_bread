from django.shortcuts import render

def product_list(request):
    return render(request, 'product_list.html')

def product_category(request):
    return render(request, 'product_category.html')

def product_detail(request):
    return render(request, 'product_detail.html')