# Generated by Django 4.2.5 on 2023-09-18 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
