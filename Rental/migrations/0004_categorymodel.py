# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-03 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0003_auto_20171103_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]