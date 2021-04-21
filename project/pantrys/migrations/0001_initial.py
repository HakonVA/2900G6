# Generated by Django 3.1.5 on 2021-04-21 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('unit', models.CharField(blank=True, max_length=8, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='recipes.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]