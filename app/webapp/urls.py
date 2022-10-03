from django.urls import path

from webapp.view.base import index_view, product_view

urlpatterns = [
    path("", index_view, name='index'),
    path("product/<int:pk>", product_view, name='product')
]
