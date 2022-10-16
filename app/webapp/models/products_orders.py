from django.db import models


class ProductOrder(models.Model):
    product = models.ForeignKey(to='webapp.Product', related_name='product_orders', on_delete=models.CASCADE, verbose_name='Product')
    order = models.ForeignKey(to='webapp.Order', related_name='order_products', on_delete=models.CASCADE, verbose_name='Order')
    count = models.IntegerField(verbose_name="Count")

    def __str__(self):
        return "{} | {}".format(self.product, self.order)

