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
        'products': products,
        'choices': Product.CHOICES
    }
    return render(request, 'index.html', context)


def choice_category_view(request, category):
    form = SearchForm(request.GET)
    if 'search' in form.data:
        if form.data['search']:
            products = Product.objects.filter(is_delete=False, category=category, title__icontains=form.data['search']).order_by('title')
        else:
            products = Product.objects.filter(is_delete=False, category=category).order_by('title')
    else:
        products = Product.objects.filter(is_delete=False, category=category).order_by('title')
    for el in products:
        el.category = el.get_category_display()
    for el in Product.CHOICES:
        if el[0] == category:
            category = el[1]
            break
    context = {
        'products': products,
        'category': category,
        'choices': Product.CHOICES
    }
    return render(request, 'category.html', context)

