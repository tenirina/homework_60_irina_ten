from django.db import models
from django.utils import timezone


class Basket(models.Model):
    product = models.ForeignKey(verbose_name="Product", to="webapp.Product", related_name="basket", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Count", null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Date of create", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date of create", auto_now=True, null=True)



