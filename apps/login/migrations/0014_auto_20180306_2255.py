# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-07 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20180306_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bday',
            field=models.DateTimeField(),
        ),
    ]
