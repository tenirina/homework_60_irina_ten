from django.urls import path

from webapp.view.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
]
