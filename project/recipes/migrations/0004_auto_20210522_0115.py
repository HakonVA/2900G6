# Generated by Django 3.1.5 on 2021-05-22 01:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_merge_20210516_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
