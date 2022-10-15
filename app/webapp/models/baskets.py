from django.db import models


class Basket(models.Model):
    product = models.ForeignKey(verbose_name="Product", to="webapp.Product", related_name="basket", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Count", null=False, blank=False)
