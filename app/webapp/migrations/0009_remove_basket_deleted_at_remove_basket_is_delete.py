# Generated by Django 4.1.1 on 2022-10-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_basket_deleted_at_basket_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='is_delete',
        ),
    ]
