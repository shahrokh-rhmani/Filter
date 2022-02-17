from django.shortcuts import render
from .models import Product
from .filters import ProductFilter



def home(request):
    # products = Product.objects.all()
    product_filter = ProductFilter(request.GET)

    context = {
        'product_filter': product_filter,
    }
    return render(request, 'home.html', context)
