# Generated by Django 3.1.5 on 2021-05-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopping',
            options={'ordering': ['user']},
        ),
        migrations.AlterField(
            model_name='shopping',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
