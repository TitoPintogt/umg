# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('municipio', '0001_initial'),
        ('aldea', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aldea',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='municipio.Municipio'),
        ),
    ]