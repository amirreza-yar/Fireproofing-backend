# Generated by Django 4.1.5 on 2023-04-25 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0017_alter_resetpassword_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='expiration_time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 25, 7, 12, 47, 590593)),
        ),
    ]
