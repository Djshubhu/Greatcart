# Generated by Django 4.1.2 on 2023-02-11 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Carts',
        ),
    ]