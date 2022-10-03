from django.shortcuts import render

from webapp.models import Product


def index_view(request):
    products = Product.objects.all()
    for el in products:
        el.category = el.get_category_display()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product_view(request, pk):
    pass
