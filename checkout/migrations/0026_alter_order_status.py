# Generated by Django 4.2 on 2023-05-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0025_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Processing', 'Processing'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')], default='Pending', max_length=150),
        ),
    ]