# Generated by Django 5.0.3 on 2024-03-26 17:40

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_bank', '0006_alter_product_description_alter_product_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(datetime.date(2024, 3, 26))], verbose_name='end_date'),
        ),
    ]