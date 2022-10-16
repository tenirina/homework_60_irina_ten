from django.urls import path

from webapp.view.base import IndexView
from webapp.view.baskets import add_basket_view, BasketView, delete_basket_view
from webapp.view.products import ProductCreateView, ProductUpdateView, ProductView, ProductDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("products/", IndexView.as_view(), name='index'),
    path("product/<int:pk>", ProductView.as_view(), name='product'),
    path("product/create", ProductCreateView.as_view(), name="create"),
    path("product/<int:pk>/edit", ProductUpdateView.as_view(), name='edit'),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(), name='delete'),
    path("products/basket/add/<int:pk>", add_basket_view, name='add_basket'),
    path("products/basket", BasketView.as_view(), name='basket'),
    path("products/basket/delete/<int:pk>", delete_basket_view, name='basket_delete')
]
