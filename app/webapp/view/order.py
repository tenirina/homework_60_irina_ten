from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, TemplateView

from webapp.forms import OrderForm, ProductOrderForm
from webapp.models import Order, Basket, ProductOrder, Product


class OrderCreateView(CreateView):
    template_name = "basket.html"
    form_class = OrderForm
    model = Order

    def form_valid(self, form):
        order_prod = Basket.objects.all()
        products_count = Product.objects.exclude(is_delete=True)
        for el in order_prod:
            for prod in products_count:
                if el.product == prod:
                    total = prod.balance - el.count
                    prod.balance = total
                    prod.save()
            product = prod.pk
            order = form.save(commit=False)
            order.product = product
            order.save()
            print(order)
        order_prod.delete()
        return redirect('index')

    def get_success_url(self):
        return reverse('index')


