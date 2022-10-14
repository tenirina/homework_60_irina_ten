from django.urls import path

from webapp.view.base import IndexView
from webapp.view.products import product_view, create_view, edit_view, delete_view, confirm_delete_view

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/<int:pk>", product_view, name='product'),
    path("create/", create_view, name="create"),
    path("product/<int:pk>/edit", edit_view, name='edit'),
    path("product/<int:pk>/delete", delete_view, name='delete'),
    path("product/<int:pk>/confirm-delete", confirm_delete_view, name='confirm_delete'),
]
