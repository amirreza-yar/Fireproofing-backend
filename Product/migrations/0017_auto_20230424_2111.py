# Generated by Django 3.2.16 on 2023-04-24 21:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0016_alter_discountcode_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 8, 21, 11, 19, 952003)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 21, 11, 19, 951688)),
        ),
    ]
