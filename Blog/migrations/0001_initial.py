# Generated by Django 4.1.5 on 2023-03-12 00:00

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, upload_to='blogImage/')),
                ('title', models.CharField(max_length=500)),
                ('en_title', models.CharField(max_length=500)),
                ('released_date', models.DateTimeField(auto_now=True)),
                ('body', ckeditor.fields.RichTextField()),
                ('en_body', ckeditor.fields.RichTextField()),
                ('meta_description', models.CharField(max_length=100)),
                ('en_meta_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rate', models.FloatField(default=5, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('commenter_name', models.CharField(max_length=200)),
                ('commenter_email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.blog')),
            ],
        ),
    ]
