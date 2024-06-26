# Generated by Django 4.1.5 on 2023-03-17 21:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0002_alter_userprofile_address_alter_userprofile_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=32, unique=True)),
                ('expiration_time', models.TimeField(default=datetime.datetime(2023, 3, 17, 21, 45, 22, 173632))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
