# Generated by Django 4.2 on 2023-05-21 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image'),
        ('carts', '0002_cart_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.variations'),
        ),
    ]