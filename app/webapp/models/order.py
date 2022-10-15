from django.db import models


class Order(models.Model):
    product = models.ManyToManyField(to="webapp.product", related_name="order", max_length=50)
    user_name = models.CharField(verbose_name="Name user", null=False, blank=False)
    phone = models.CharField(verbose_name="Phone user", null=False, blank=False)
    address = models.CharField(verbose_name="Address user", null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Date of create", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date of create", auto_now=True, null=True)
    is_delete = models.BooleanField(verbose_name="Delete", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name="Date of delete", null=True, default=None)
