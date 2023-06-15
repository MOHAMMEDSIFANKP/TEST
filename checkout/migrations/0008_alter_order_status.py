# Generated by Django 4.2 on 2023-05-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out For Shipping', 'Out For Shipping'), ('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=150),
        ),
    ]
