from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, TemplateView

from webapp.forms import OrderForm, ProductOrderForm
from webapp.models import Order, Basket, ProductOrder


class OrderCreateView(CreateView):
    template_name = "basket.html"
    form_class = OrderForm
    model = Order

    def get_success_url(self):
        return reverse('order_product_create', kwargs={'pk': self.object.pk})


class OrderProductCreateView(CreateView):
    model = ProductOrder
    form_class = ProductOrderForm
    template_name = "products/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("I'm here gggg")
        print(kwargs)
        return context

    def form_valid(self, form):
        order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        print(order)
        product = form.save(commit=False)
        product.order = order
        print('jdjjdjj')
        print(product.order)
        return redirect('products/index')

    def form_invalid(self, form):
        print("I'm here")
        return redirect('products/index.html')

    def get_redirect_url(self):
        return reverse('index')
