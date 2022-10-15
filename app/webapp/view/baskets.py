from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from webapp.models import Product, Basket


def add_basket_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_product = Basket.objects.filter(product=product.pk)
    if len(basket_product) == 0 and product.balance != 0:
        data = {
            'product': product,
            'count': 1
        }
        Basket.objects.create(**data)
    elif len(basket_product) != 0:
        if basket_product[0].count < product.balance:
            basket_product = get_object_or_404(Basket, pk=basket_product[0].pk)
            basket_product.count += 1
            basket_product.save()
    print(Basket.objects.filter(product=product.pk))
    return redirect('index')


class BasketView(ListView):
    template_name = "basket.html"
    model = Basket
    context_object_name = "products"