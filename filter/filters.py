import django_filters
from .models import Product



class ProductFilter(django_filters.FilterSet):
    quantity = django_filters.AllValuesFilter()

    class Meta:
        model = Product
        fields = ['quantity']
