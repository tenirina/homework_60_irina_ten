from django.shortcuts import get_object_or_404, render

from webapp.models import Product


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.category = product.get_category_display()
    return render(request, 'product.html', context={'product': product})
