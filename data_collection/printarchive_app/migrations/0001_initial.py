# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-17 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=200)),
                ('page_num', models.PositiveSmallIntegerField(default=0)),
                ('page_date', models.DateField(blank=True, null=True)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
