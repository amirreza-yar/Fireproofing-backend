# Generated by Django 4.1.5 on 2023-04-24 22:06

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
            field=models.DateField(default=datetime.datetime(2023, 5, 8, 22, 6, 17, 924780)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 24, 22, 6, 17, 924374)),
        ),
    ]