# Generated by Django 3.1.5 on 2021-05-02 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
        ('shoppinglists', '0002_auto_20210502_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='recipes',
        ),
        migrations.AddField(
            model_name='shoppingentry',
            name='recipes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='recipes.recipe'),
        ),
    ]