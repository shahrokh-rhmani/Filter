from django.shortcuts import render
from .models import Product



def home(request):
    products = Product.objects.all()

    context = {
        'product': products
    }
    return render(request, 'home.html', context)
