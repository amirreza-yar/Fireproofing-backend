# Generated by Django 4.1.5 on 2023-03-18 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0004_alter_resetpassword_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='expiration_time',
            field=models.TimeField(default=datetime.datetime(2023, 3, 18, 18, 2, 32, 897874)),
        ),
    ]
