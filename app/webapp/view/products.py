from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductCreateView(CreateView):
    template_name = "products/create.html"
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = "products/edit.html"
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    def get_success_url(self):
        return reverse("product", kwargs={'pk': self.object.pk})


class ProductView(DetailView):
    template_name = "products/product.html"
    model = Product


class ProductDeleteView(DeleteView):
    template_name = "products/confirm_delete.html"
    model = Product
    success_url = reverse_lazy('index')


