# Generated by Django 3.2.12 on 2023-06-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0047_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Return', 'Return'), ('Shipped', 'Shipped')], default='Pending', max_length=150),
        ),
    ]
