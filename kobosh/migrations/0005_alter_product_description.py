# Generated by Django 4.2.1 on 2023-05-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobosh', '0004_product_product_kobosh_prod_id_15bd1a_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
