# Generated by Django 3.2.23 on 2024-01-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_baket_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
