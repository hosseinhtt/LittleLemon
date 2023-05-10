# Generated by Django 4.2.1 on 2023-05-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]