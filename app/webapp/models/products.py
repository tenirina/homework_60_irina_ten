from django.db import models

from django.utils import timezone


class Product(models.Model):

    class CategoryChoices(models.TextChoices):
        OTHER = "other", "Other"
        FRUITS = "fruits", "Fruits"
        VEGETABLES = "vegetables", "Vegetables"
        PREPARED = "prepared", "Prepared food"

    title = models.CharField(verbose_name="Title", max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name="Description", max_length=2000, null=True, blank=False)
    photo = models.CharField(verbose_name="Photo", max_length=200, null=True, blank=False)
    category = models.CharField(verbose_name="Category", max_length=100, null=False, blank=False, choices=CategoryChoices.choices)
    balance = models.IntegerField(verbose_name="Balance", null=False, blank=False)
    price = models.DecimalField(verbose_name="Price", max_digits=9, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Date of create", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date of create", auto_now=True, null=True)
    is_delete = models.BooleanField(verbose_name="Delete", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name="Date of delete", null=True, default=None)
    order = models.ManyToManyField(to="webapp.Order", related_name="products", through="webapp.ProductOrder", through_fields=("product", "order"))

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_delete = True
        self.save()



