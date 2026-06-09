from django.shortcuts import render, get_object_or_404
from .models import Product

def shop_home(request):
    category = request.GET.get('category', 'all')
    
    if category == 'all':
        products = Product.objects.filter(available=True)
    else:
        products = Product.objects.filter(available=True, category=category)
    
    context = {
        'products': products,
        'current_category': category,
    }
    return render(request, 'shop/home.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    context = {
        'product': product,
    }
    return render(request, 'shop/detail.html', context)