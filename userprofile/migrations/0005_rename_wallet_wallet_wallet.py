# Generated by Django 4.2 on 2023-06-05 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_rename_walet_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='Wallet',
            new_name='wallet',
        ),
    ]