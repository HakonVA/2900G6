# Generated by Django 3.1.5 on 2021-05-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='recipes/'),
        ),
    ]