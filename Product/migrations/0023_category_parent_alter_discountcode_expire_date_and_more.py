# Generated by Django 4.1.5 on 2023-05-23 05:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0022_category_en_description_category_en_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Product.category'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 5, 47, 43, 478856)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 5, 47, 43, 478441)),
        ),
    ]