# Generated by Django 3.2.16 on 2023-07-16 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0020_alter_resetpassword_expiration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='expiration_time',
            field=models.TimeField(default=datetime.datetime(2023, 7, 16, 21, 59, 19, 131002)),
        ),
    ]