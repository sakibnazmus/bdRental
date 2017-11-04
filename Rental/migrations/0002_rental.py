# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-03 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField()),
                ('advance', models.IntegerField()),
                ('contact', models.CharField(max_length=17)),
                ('details', models.TextField(max_length=200)),
                ('available_from', models.DateField()),
                ('available_upto', models.DateField(blank=True, null=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Rental.LocationModel')),
            ],
        ),
    ]
