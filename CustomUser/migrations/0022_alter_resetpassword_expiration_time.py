# Generated by Django 4.2 on 2023-07-16 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0021_alter_resetpassword_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='expiration_time',
            field=models.TimeField(default=datetime.datetime(2023, 7, 16, 23, 37, 56, 760030)),
        ),
    ]
