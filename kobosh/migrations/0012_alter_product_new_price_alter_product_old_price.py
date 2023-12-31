# Generated by Django 4.2.1 on 2023-06-06 13:57

from django.db import migrations, models
import kobosh.models


class Migration(migrations.Migration):

    dependencies = [
        ('kobosh', '0011_alter_product_new_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=kobosh.models.CommaSeparatedIntegerField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
