# Generated by Django 4.2 on 2023-05-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Out For Shipping', 'Out For Shipping'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
