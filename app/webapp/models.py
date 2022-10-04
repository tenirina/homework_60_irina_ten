from django.db import models


class Product(models.Model):
    CHOICES = (
        ("other", "Other"),
        ("fruits", "Fruits"),
        ("vegetables", "Vegetables"),
        ("prepared", "Prepared food")
    )

    title = models.CharField(verbose_name="Title", max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name="Description", max_length=2000, null=True, blank=False)
    photo = models.CharField(verbose_name="Photo", max_length=200, null=True, blank=False)
    category = models.CharField(verbose_name="Category", max_length=100, null=False, blank=False, choices=CHOICES)
    balance = models.IntegerField(verbose_name="Balance", null=False, blank=False)
    price = models.DecimalField(verbose_name="Price", max_digits=9, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Date of create", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date of create", auto_now=True, null=True)
    is_delete = models.BooleanField(verbose_name="Delete", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name="Date of delete", null=True, default=None)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

