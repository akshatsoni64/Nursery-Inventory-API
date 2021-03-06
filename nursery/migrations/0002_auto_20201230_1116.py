# Generated by Django 3.1.4 on 2020-12-30 11:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantmodel',
            name='image',
            field=models.ImageField(default='static/default.jpg', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='plantmodel',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
