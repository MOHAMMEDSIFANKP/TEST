# Generated by Django 4.2 on 2023-05-29 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_price_filter_product_price_range'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='price_filter',
            new_name='PriceFilter',
        ),
    ]
