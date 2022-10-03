from django.shortcuts import render

from webapp.forms import SearchForm
from webapp.models import Product


def index_view(request):
    form = SearchForm(request.GET)
    if 'search' in form.data:
        if form.data['search']:
            products = Product.objects.filter(is_delete=False, balance__gt=1, title__icontains=form.data['search']).order_by('category', 'title')
        else:
            products = Product.objects.filter(is_delete=False, balance__gt=1).order_by('category', 'title')
    else:
        products = Product.objects.filter(is_delete=False, balance__gt=1).order_by('category', 'title')
    for el in products:
        el.category = el.get_category_display()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def product_view(request, pk):
    pass
