# Generated by Django 4.1.5 on 2023-04-23 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0012_alter_resetpassword_expiration_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='field',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profileImage/'),
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='expiration_time',
            field=models.TimeField(default=datetime.datetime(2023, 4, 23, 17, 16, 38, 418357)),
        ),
    ]
