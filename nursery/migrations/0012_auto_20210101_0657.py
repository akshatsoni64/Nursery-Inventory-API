# Generated by Django 3.1.4 on 2021-01-01 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0011_auto_20210101_0535'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderModel',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='PlantModel',
            new_name='Plant',
        ),
    ]
