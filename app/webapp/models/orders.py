from django.db import models


class Order(models.Model):
    user_name = models.CharField(verbose_name="Name user", null=False, blank=False, max_length=50)
    phone = models.CharField(verbose_name="Phone user", null=False, blank=False, max_length=15)
    address = models.CharField(verbose_name="Address user", null=False, blank=False, max_length=100)
    created_at = models.DateTimeField(verbose_name="Date of create", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date of create", auto_now=True, null=True)
    is_delete = models.BooleanField(verbose_name="Delete", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name="Date of delete", null=True, default=None)
