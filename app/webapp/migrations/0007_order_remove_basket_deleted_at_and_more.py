# Generated by Django 4.1.1 on 2022-10-16 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_basket_created_at_basket_deleted_at_basket_is_delete_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='Name user')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone user')),
                ('address', models.CharField(max_length=100, verbose_name='Address user')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of create')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date of create')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Date of delete')),
            ],
        ),
        migrations.RemoveField(
            model_name='basket',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='is_delete',
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='webapp.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_orders', to='webapp.product', verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ManyToManyField(related_name='products', through='webapp.ProductOrder', to='webapp.order'),
        ),
    ]
