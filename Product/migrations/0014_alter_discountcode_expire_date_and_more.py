# Generated by Django 4.1.5 on 2023-03-18 20:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_alter_discountcode_expire_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 1, 20, 45, 4, 655277)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 20, 45, 4, 655011)),
        ),
    ]
