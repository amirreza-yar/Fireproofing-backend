# Generated by Django 4.2 on 2023-07-17 00:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0025_alter_discountcode_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 0, 4, 4, 583521)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 0, 4, 4, 583071)),
        ),
    ]