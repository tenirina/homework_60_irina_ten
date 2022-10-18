from django.shortcuts import  redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView

from webapp.forms import OrderForm
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
    queryset = Basket.objects.exclude(is_delete=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        total_count = 0
        total = 0
        for el in Basket.objects.all():
            total += el.product.price*el.count
            total_count += el.count
        context['total'] = total
        context['total_count'] = total_count
        context['form'] = OrderForm
        return context


class BasketDeleteView(DeleteView):
    template_name = "basket.html"
    model = Basket
    success_url = reverse_lazy('index')
    queryset = Basket.objects.exclude(is_delete=True)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('basket')
