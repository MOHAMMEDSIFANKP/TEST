# Generated by Django 4.2 on 2023-06-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0035_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Shipped', 'Shipped'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
