# Generated by Django 3.2.23 on 2024-01-05 10:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_baket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Baket',
            new_name='Basket',
        ),
    ]
