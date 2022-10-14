from django.views.generic import ListView

from webapp.models import Product


class IndexView(ListView):
    template_name = "products/index.html"
    model = Product
    context_object_name = "products"
    paginate_by = 6
    paginate_orphans = 2
    queryset = Product.objects.exclude(is_delete=True)



