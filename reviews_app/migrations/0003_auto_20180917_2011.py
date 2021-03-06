# Generated by Django 2.1.1 on 2018-09-17 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0002_auto_20180915_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(0.5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='submission_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='summary',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
